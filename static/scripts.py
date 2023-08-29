def makeMap(df, title, value):
    font = 'arial, serif'
    width = 500
    height = 300

    chart_title = alt.TitleParams(
        "Firearm Death Rates per 100,000 Population (2020)",
        fontSize=20,
        font=font,
        subtitleColor="green",
        subtitleFontSize=14
    )

    heatmap = alt.Chart(df, title=title).mark_rect(stroke=None).encode(
        x=alt.X('col:O', axis=None, scale=alt.Scale(range=[0, width])),
        y=alt.Y('row:O', axis=None, scale=alt.Scale(range=[0, height])),
        color=alt.Color(value, scale=alt.Scale(scheme='blueorange'))
    )

    text = heatmap.mark_text(baseline='middle', align='center', fill='black', fontSize=14).encode(
        text='code:O'
    )

    mapchart = (heatmap + text).properties(width=width, height=height)

    # display the chart
    return mapchart.to_json()


df = pd.read_csv('static/mapData.csv', delimiter=',')