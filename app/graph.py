import altair as alt


def chart(df, X, Y, target) -> alt.Chart:
    alt.themes.enable('dark')
    title = f'{Y} by {X} for {target}'
    ch = alt.Chart(df, title=title).mark_point().encode(
        x=X,
        y=Y,
        color=target,
        tooltip=['Name', 'Type', 'Level', 'Rarity',
                 'Damage', 'Health', 'Energy', 'Sanity', 'Timestamp']

    ).properties(
        width=600,
        height=600
    )
    return ch
