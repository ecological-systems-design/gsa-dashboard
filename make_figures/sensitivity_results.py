import pandas as pd
import numpy as np

# Local files
from .utils import get_figure_layout


def plot_model_linearity(linearity=None, linearity_threshold=0.8):
    data = []
    layout = get_figure_layout()
    data.append(dict(
        type="scatter", x=[0, 10], y=[1, 1],
        mode="lines", line=dict(color="red", dash="dash"),
        name="Linear model", showlegend=True,
    ))
    data.append(dict(
        type="scatter", x=[0, 10], y=[linearity_threshold, linearity_threshold],
        mode="lines", line=dict(color="orange", dash="dash"),
        name="Apprx. linear model", showlegend=True,
    ))
    data.append(dict(
        type="scatter", x=[None], y=[None],
        mode="markers+lines", marker=dict(symbol="x", size=10, color="blue"),
        name="SRCs of LCA model", showlegend=True,
    ))
    layout["xaxis"]["title"].update(dict(text="Monte Carlo iterations"))
    layout["yaxis"]["title"].update(dict(text="Degree of linearity"))
    layout["yaxis"]["range"] = [-0.1, 1.2]
    layout["height"] = 220
    layout["legend"].update(dict(
        x=1.1, xanchor="left",
        y=0.5, yanchor="middle",
        orientation="v"),
    )
    layout["margin"].update(dict(l=50, b=50, r=0, t=0))

    if linearity is not None:
        iterations = list(linearity.keys())
        data[0]["x"] = [0, iterations[-1]]
        data[1]["x"] = [0, iterations[-1]]
        data[2]["x"] = iterations
        data[2]["y"] = list(linearity.values())

    return dict(data=data, layout=layout)


def create_table_gsa_ranking(data=None):
    if data is None:
        n_entries = 81
        df_data = {
            "GSA rank": list(range(1, n_entries+1)),
            "LCA model input": [None]*n_entries,
            "Amount": [None]*n_entries,
            "Type": [None]*n_entries,
            "GSA index": [None]*n_entries,
            "Contribution": [None]*n_entries,
        }
        df = pd.DataFrame.from_dict(df_data)
    else:
        n_entries = len(data["GSA index"])
        inputs = []
        for i in range(n_entries):
            input_loc = data["Input location"][i]
            input_location = f", {input_loc}" if input_loc is not None else ""
            input_cat = data["Input categories"][i]
            input_category = f", {input_cat}" if input_cat is not None else ""
            output_loc = data["Output location"][i]
            output_location = f", {output_loc}" if output_loc is not None else ""
            input_ = f"FROM {data['Input name'][i]}{input_location}{input_category} \n   TO {data['Output name'][i]}{output_location}"
            inputs.append(input_)
        df_data = {
            "LCA model input": inputs,
            "Amount": data["Exchange amount"],
            "Type": data["Exchange type"],
            "GSA index":  list(data["GSA index"]),
            "Contribution": [None]*n_entries,
        }
        df = pd.DataFrame.from_dict(df_data)
        df = df.sort_values(by="GSA index", axis=0, ascending=False).reset_index(drop=True)
        columns = df.columns.tolist()
        df["GSA rank"] = np.arange(1, len(df)+1)
        columns = ["GSA rank"] + columns
        df = df[columns]
    df_data = df.to_dict("records")
    columns = [{"name": i, "id": i} for i in df.columns]
    return df_data, columns


def plot_gsa_ranking(sensitivity_indices=None):
    data = []
    if sensitivity_indices is not None:
        data = sensitivity_indices
    layout = get_figure_layout()
    layout["xaxis"]["title"].update(dict(text="Sensitivity index"))
    layout["yaxis"]["title"].update(dict(text="Model input"))
    layout["height"] = 400
    return dict(data=data, layout=layout)


# import pandas as pd
# from dash import html
#
#
# def get_prioritized_list():
#     df = pd.read_excel("make_figures/data/GSA_results.xlsx")
#     df = df[["input_names", "output_names", "spearman"]]
#     df = df.reset_index()
#     df.columns = ["", "input", "output", "spearman"]
#     df['spearman'] = [f"{val:.3f}" for val in df['spearman']]
#     return df
#
#
# def generate_table(dataframe, max_rows=20):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])