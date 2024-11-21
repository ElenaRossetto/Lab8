import polars as pl
import altair as alt # per creare grafici
import streamlit as st

data_url = 'https://www.dei.unipd.it/~ceccarello/data/gapminder.csv'

gapminder = pl.read_csv(data_url)
st.write(gapminder)

alt.X('year').scale(zero=False)

# es 1
chart = (
    alt.Chart(gapminder)   
    .mark_point()  
    .encode(
        alt.X('year').scale(zero=False),   # per togliere lo zero dall'asse x, e lasciare l'asse x più 'libera'
        alt.Y('lifeExp')
    )
)

st.altair_chart( 
    chart,
    use_container_width=True 
)
# life expencancy aumenta all'aumentare degli anni


# es 2
chart = (
    alt.Chart(gapminder)   
    .mark_line()  
    .encode(
        alt.X('year').scale(zero=False),   # per togliere lo zero dall'asse x, e lasciare l'asse x più 'libera'
        alt.Y('lifeExp', aggregate='mean')
    )
)

st.altair_chart( 
    chart,
    use_container_width=True 
)


# es 3
chart = (
    alt.Chart(gapminder)   
    .mark_line()  
    .encode(
        alt.X('year').scale(zero=False),   # per togliere lo zero dall'asse x, e lasciare l'asse x più 'libera'
        alt.Y('lifeExp', aggregate='mean').scale(zero=False),   # oppure domain=[30, 85] per determinare il dominio dell'asse in modo preciso
        alt.Color('continent')
    )
)

st.altair_chart( 
    chart,
    use_container_width=True 
)

# praticamente stiamo calcolando la media di ogni continente per ogni anno

# es 4
gapminder7 = pl.read_csv(data_url).filter(pl.col('year')==2007)

chart = (
    alt.Chart(gapminder)   
    .mark_arc()  
    .encode(
        alt.Theta('pop', aggregate='sum'),  # aggregate='sum' per fare in modo venga fuori tutto unito, e non le varie linee che separano gli stati
        alt.Color('continent')
    )
)

st.altair_chart( 
    chart,
    use_container_width=True 
)



# es 5
chart = (
    alt.Chart(gapminder)   
    .mark_arc(radius=80, radius2=130, cornerRadius=10)  
    .encode(
        alt.Theta('pop', aggregate='sum'),  # aggregate='sum' per fare in modo venga fuori tutto unito, e non le varie linee che separano gli stati
        alt.Color('continent')
    )
)

st.altair_chart( 
    chart,
    use_container_width=True 
)
