import plotly.graph_objects as go

def temperature_graph(
temperature,
C_conversion,
P_conversion,
reactor_type
):

    fig = go.Figure()

    if reactor_type == "CSTR":

        fig.add_trace(
            go.Scatter(
                x=temperature,
                y=C_conversion,
                mode="lines",
                name="CSTR"
            )
        )

    elif reactor_type == "PFR":

        fig.add_trace(
            go.Scatter(
                x=temperature,
                y=P_conversion,
                mode="lines",
                name="PFR"
            )
        )

    else:

        fig.add_trace(
            go.Scatter(
                x=temperature,
                y=C_conversion,
                mode="lines",
                name="CSTR"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=temperature,
                y=P_conversion,
                mode="lines",
                name="PFR"
            )
        )

    fig.update_layout(
        title="Conversion vs Temperature",
        xaxis_title="Temperature (K)",
        yaxis_title="Conversion"
    )

    return fig


def volume_graph(
volume_list,
C_conversion,
P_conversion,
reactor_type
):

    fig = go.Figure()

    if reactor_type == "CSTR":

        fig.add_scatter(
            x=volume_list,
            y=C_conversion,
            mode="lines",
            name="CSTR"
        )

    elif reactor_type == "PFR":

        fig.add_scatter(
            x=volume_list,
            y=P_conversion,
            mode="lines",
            name="PFR"
        )

    else:

        fig.add_scatter(
            x=volume_list,
            y=C_conversion,
            mode="lines",
            name="CSTR"
        )

        fig.add_scatter(
            x=volume_list,
            y=P_conversion,
            mode="lines",
            name="PFR"
        )

    fig.update_layout(
        title="Conversion vs Volume",
        xaxis_title="Volume (m³)",
        yaxis_title="Conversion"
    )

    return fig