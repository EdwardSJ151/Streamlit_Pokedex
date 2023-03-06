import streamlit as st
import pandas as pd
import plotly.express as px
pokemon = pd.read_csv(r'C:\Users\dival\Downloads\pokemon_dataset\pkdx_2.csv')

st.title('Outras Funcionalidades')
tab1, tab2, tab3 = st.tabs(['st.plotly_chart', 'st.metric/st.expander', 'st.slider'])

with tab1:
    st.subheader('Análise da quantidade de tipos para cada geração')
    fig_GenToType = px.treemap(pokemon, path=['generation', 'type_1'], hover_data=['type_1'])
    st.plotly_chart(fig_GenToType)
    st.markdown('***')

    st.subheader('Análise da correlação entre tipos de um Pokémon')
    type1, type2, type3 = st.columns(3)
    pokemon['type_2'] = pokemon['type_2'].fillna('Monotype')
    type1.write('')
    tipo = type2.selectbox('Tipo de gráfico:', ('Tipo 1 para 2', 'Tipo 2 para 1'))
    type3.write('')
    if tipo == 'Tipo 1 para 2':
        fig_Type1To2 = px.treemap(pokemon, path=['type_1', 'type_2'], hover_data=['type_2'])
        st.plotly_chart(fig_Type1To2)
    elif tipo == 'Tipo 2 para 1':
        fig_Type2To1 = px.treemap(pokemon, path=['type_2', 'type_1'], hover_data=['type_1'])
        st.plotly_chart(fig_Type2To1)
    st.markdown('***')

    st.subheader('Top 30 Pokémons com maior tot de valores de batalha base')
    dfstrong = pokemon.groupby('name')['total_points'].sum().reset_index().sort_values('total_points',ascending =False)
    figstrong = px.bar(dfstrong[:30], y='total_points', x='name', color='total_points', height=600)
    st.plotly_chart(figstrong)
    st.markdown('***')

with tab2:
    st.subheader('Algumas Cotações de Hoje')
    st.write('')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('BTC', '120.694,61', '+18.059,35 (17,60%)')
        with st.expander('Mais sobre BTC'):
            st.write('Bitcoin (BTC) é uma criptomoeda livre e descentralizada, um dinheiro eletrônico para transações '
                     'financeiras ponto a ponto (sem intermediários)')
    with col2:
        st.metric('Ibovespa', '103.164,69', '+568,03 (0,55%)')
        with st.expander('Mais sobre Ibovespa'):
            st.write('Índice Bovespa (Ibovespa) é o mais importante indicador do desempenho médio das cotações das '
                     'ações negociadas na B3 - Brasil, Bolsa, Balcão. É formado pelas ações com maior volume '
                     'negociado nos últimos meses.')
    with col3:
        st.metric('Netflix', '224,90', '-1,12 (0,50%)')
        with st.expander('Mais sobre Netflix'):
            st.write('Netflix é uma provedora global de filmes e séries de televisão via streaming.')
    st.caption('Cotação pego do dia 31/07/2022')

with tab3:
    st.subheader('Slider que mostra imagens')
    pokeimage = st.slider('Use o slider para ver um Pokémon', 1, 151, 25)
    st.markdown(f"![Sugimori](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokeimage}.png)")
