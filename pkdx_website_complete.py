# Bibliotecas e Frameworks
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import requests
import json

# Criando duas abas para navegar no site
menu = option_menu(
    menu_title='Pokédex',
    options=['Dados dos Pokémons', 'Dados dos Ataques'],
    icons=['dpad', 'book'],
    menu_icon='nintendo-switch',
    orientation='horizontal',
)

# Dados dos Pokémons
if menu == 'Dados dos Pokémons':
    # Leitura e formatação do dataset
    # tabela2 = pd.read_csv(r'C:\Users\dival\Downloads\pokemon_dataset\pkdx_2.csv')
    tabela2 = pd.read_csv('pokemon_dataset/pkdx_2.csv')
    tabela2 = tabela2.drop(['Unnamed: 0'], axis=1)
    tabela2_num = tabela2.groupby('pokedex_number').first()
    lista2 = tabela2_num.values.tolist()
    tabela2_num = lista2
    # st.dataframe(lista2)
    # st.dataframe(tabela2)
    # st.dataframe(tabela2_num)

    st.sidebar.title('Configurações da Pokédex')
    # Deixar o usuário escrever o nome do Pokémon ou pesquisar pelo seu número de identificação
    nome_input = st.sidebar.checkbox('Clicar para escrever nome do Pokémon para pesquisar.')
    if nome_input:
        pokemon = 1
    else:
        pass
    if nome_input:
        pokemon_name = st.sidebar.text_input('Insira o nome do pokemon na pokédex: ').title().strip()
        for c in range(0, 889):
            if pokemon_name == tabela2_num[c][0]:
                pokemon = c + 1
    else:
        pokemon = st.sidebar.number_input('Insira número na pokédex: ', value=int(1))

    # Pokemon API
    entry_dict = {}
    url_api = 'https://pokeapi.co/api/v2/pokemon-species/'
    pokemon_api = str(pokemon)
    pokemon_url = url_api + pokemon_api
    pokemon_request = requests.get(pokemon_url)
    data = pokemon_request.text
    parse_json = json.loads(data)
    flavor_text_wip = parse_json["flavor_text_entries"]

    for c in range(0, len(flavor_text_wip)):
        if parse_json["flavor_text_entries"][c]['language']['name'] == 'en':
            game_add = parse_json["flavor_text_entries"][c]['version']['name']
            entry_dict[parse_json["flavor_text_entries"][c]['version']['name']] = parse_json["flavor_text_entries"][c]["flavor_text"]

    entry = {k.capitalize(): v for k, v in entry_dict.items()}

    for key in entry.keys():
        entry[key] = entry[key].replace(r'\n', '')
        entry[key] = entry[key].replace('\x0c', ' ')

    # Preparando listas e nome das fraquezas do site
    weakness_names = ['Normal/Normal', 'Fire/Fogo', 'Water/Água', 'Electric/Elétrico', 'Grass/Grama', 'Ice/Gelo',
                      'Fighting/Lutador', 'Poison/Venenoso', 'Ground/Terra', 'Flying/Voador', 'Psychic/Psíquico',
                      'Bug/Inseto', 'Rock/Pedra', 'Ghost/Fantasma', 'Dragon/Dragão', 'Dark/Sombrio', 'Steel/Metal',
                      'Fairy/Fada']
    weakness_append = []
    weakness = []

    # Montando o sidebar
    geracao = st.sidebar.selectbox(
        'Geração',
        ('Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6', 'Gen 7', 'Gen 8'))
    artwork = st.sidebar.selectbox(
        'Arte oficial',
        ('Ilustrações Sugimori', 'Pokémon HOME', 'Dream World'))
    libras = st.sidebar.checkbox('Clicar para ver peso em libras.')
    sis_med_usa = st.sidebar.checkbox('Clicar para ver altura em polegadas.')
    femea = st.sidebar.checkbox('Clicar para ver porcentagem fêmea.')
    avancado = st.sidebar.checkbox('Clicar para ver mais dados.')
    masculino = tabela2_num[pokemon - 1][29]

    # Verificando se um Pokémon existia em uma determinada geração
    st.write('***')
    if pokemon == int(0):
        st.write('Digite o número do pokémon')
    elif pokemon < int(891):
        st.title(f'{tabela2_num[pokemon - 1][0]} - PKMN N°{pokemon}')
        if geracao == 'Gen 1' and pokemon > 151:
            st.write(f'O pokémon {tabela2_num[pokemon - 1][0]} não pertence a essa geração.  ')
            st.write('Essa geração vai do pokémon número 1 atê 151.')
        elif geracao == 'Gen 2' and pokemon > 251:
            st.write(f'O pokémon {tabela2_num[pokemon - 1][0]} não pertence a essa geração.  ')
            st.write('Essa geração vai do pokémon número 1 atê 251.')
        elif geracao == 'Gen 3' and pokemon > 386:
            st.write(f'O pokémon {tabela2_num[pokemon - 1][0]} não pertence a essa geração.  ')
            st.write('Essa geração vai do pokémon número 1 atê 386.')
        elif geracao == 'Gen 4' and pokemon > 493:
            st.write(f'O pokémon {tabela2_num[pokemon - 1][0]} não pertence a essa geração.  ')
            st.write('Essa geração vai do pokémon número 1 atê 493.')
        elif geracao == 'Gen 5' and pokemon > 649:
            st.write(f'O pokémon {tabela2_num[pokemon - 1][0]} não pertence a essa geração.  ')
            st.write('Essa geração vai do pokémon número 1 atê 649.')
        elif geracao == 'Gen 6' and pokemon > 721:
            st.write(f'O pokémon {tabela2_num[pokemon - 1][0]} não pertence a essa geração.  ')
            st.write('Essa geração vai do pokémon número 1 atê 721.')
        elif geracao == 'Gen 7' and pokemon > 809:
            st.write(f'O pokémon {tabela2_num[pokemon - 1][0]} não pertence a essa geração.  ')
            st.write('Essa geração vai do pokémon número 1 atê 809.')
        else:
            # Mostrando a arte do Pokémon
            col1data, col2data, col3data = st.columns(3)
            with col1data:
                if artwork == 'Ilustrações Sugimori':
                    st.markdown(f"![Sugimori](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon}.png)")
                elif artwork == 'Pokémon HOME':
                    st.markdown(f"![HOME](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{pokemon}.png)")
                else:
                    if pokemon > int(646):
                        st.write('Não existe arte deste pokémon no Dream World')
                    else:
                        st.markdown(f"![Dream World](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{pokemon}.svg)")
            with col2data:
                st.write('')
            with col3data:
                st.write('---')

                # Dados básicos de cada Pokémon (O dataset não tinha muita coisa sobre Pokémons da oitava geração)
                st.markdown("###     Dados do Pokémon")
                # st.markdown("<h3 style='text-align: center;'>Dados do Pokémon</h3>", unsafe_allow_html=True)
                if geracao == 'Gen 8':
                    pass
                else:
                    if avancado:
                        st.markdown(f'- Nome em japonês : {tabela2_num[pokemon - 1][2]}')
                        st.markdown(f'- Nome em alemão : {tabela2_num[pokemon - 1][1]}')
                st.markdown(f'- The {tabela2_num[pokemon - 1][5]}')
                if pd.isnull(tabela2_num[pokemon - 1][13]) == True:
                    st.markdown(f'- Habilidade : {tabela2_num[pokemon - 1][12]}')
                else:
                    st.markdown(f'- Habilidade : {tabela2_num[pokemon - 1][12]} / {tabela2_num[pokemon - 1][13]}')
                if pd.isnull(tabela2_num[pokemon - 1][14]) == True:
                    pass
                else:
                    if avancado:
                        st.markdown(f'- Habilidade escondida : {tabela2_num[pokemon - 1][14]}')
                if pd.isnull(tabela2_num[pokemon - 1][8]) == True:
                    st.markdown(f'- Tipo : {tabela2_num[pokemon - 1][7]}')
                else:
                    st.markdown(f'- Tipo : {tabela2_num[pokemon - 1][7]}/{tabela2_num[pokemon - 1][8]}')
                if sis_med_usa:
                    st.markdown(f'- Altura em polegadas : {39.37 * tabela2_num[pokemon - 1][9]:.1f}in')
                else:
                    st.markdown(f'- Altura em metros : {tabela2_num[pokemon - 1][9]:.1f}m')
                if libras:
                    st.markdown(f'- Peso em libras : {2.2046 * tabela2_num[pokemon - 1][10]:.1f}lbs')
                else:
                    st.markdown(f'- Peso em kg : {tabela2_num[pokemon - 1][10]:.1f}kg')
                if femea:
                    st.markdown(f'- Porcentagem ♀ : %{100 - tabela2_num[pokemon - 1][29]:.1f}')
                else:
                    st.markdown(f'- Porcentagem ♂ : %{tabela2_num[pokemon - 1][29]:.1f}')
            if tabela2_num[pokemon - 1][29] == 0:
                st.subheader(f'Voz da {tabela2_num[pokemon - 1][0]}')
            else:
                st.subheader(f'Voz do {tabela2_num[pokemon - 1][0]}')
            if pokemon == 25:
                st.write('O Pikachu é um caso especial, ele é o único Pokémon com mais de um arquivo de voz. '
                         'Ele também é o único com uma voz que não é composto por barulhos eletrônicos.')
                pikacry = st.slider('Use o slider para escolher uma voz: ', 1, 97)
                # cry = open(r'C:\Users\dival\Downloads\pokemon_cries\pikachu' + '//' + f'{pikacry}.wav', 'rb')
                cry = open('pokemon_cries/pikachu' + '//' + f'{pikacry}.wav', 'rb')
                st.audio(cry)
            else:
                # cry = open(r'C:\Users\dival\Downloads\pokemon_cries\cries_pokedex' + '//' + f'{pokemon}.wav', 'rb')
                cry = open('pokemon_cries/cries_pokedex' + '//' + f'{pokemon}.wav', 'rb')
                st.audio(cry)
            st.write('***')

            # Imprimindo os dados que peguei da API
            # O if é quando eu faço print de todas as entradas do API
            # O else é quando eu só pego entradas da geração selecionada
            st.header('Entradas na Pokédex')
            if avancado:
                for key, values in entry.items():
                    pkdx_entry = key, ': ', values
                    col1dexavancado, col2dexavancado, col3dexavancado, col4dexavancado, col5dexavancado = st.columns(5)
                    st.write(''.join(pkdx_entry))
                    col1dexavancado.write('')
                    col2dexavancado.write('')
                    with col3dexavancado:
                        if pokemon > 809:
                            st.markdown(f"![SwShSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/{pokemon}.png)")
                        else:
                            st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                    col4dexavancado.write('')
                    col5dexavancado.write('')
            else:
                col1dex, col2dex, col3dex, col4dex, col5dex = st.columns(5)
                col1dex.write('')
                col2dex.write('')
                with col3dex:
                    if pokemon > 809:
                        st.markdown(f"![SwShSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/{pokemon}.png)")
                    else:
                        st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                col4dex.write('')
                col5dex.write('')
                for key, values in entry.items():
                    pkdx_entry = key, ': ', values
                    if geracao == 'Gen 1':
                        if 'Red' in key or 'Blue' in key or 'Yellow' in key:
                            st.markdown(''.join(pkdx_entry))
                            col1gen1, col2gen1, col3gen1, col4gen1, col5gen1 = st.columns(5)
                            col1gen1.write('')
                            col2gen1.write('')
                            with col3gen1:
                                st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            col4gen1.write('')
                            col5gen1.write('')
                    if geracao == 'Gen 2':
                        if 'Gold' in key or 'Silver' in key or 'Crystal' in key:
                            st.markdown(''.join(pkdx_entry))
                            col1gen2, col2gen2, col3gen2, col4gen2, col5gen2 = st.columns(5)
                            col1gen2.write('')
                            col2gen2.write('')
                            with col3gen2:
                                st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            col4gen2.write('')
                            col5gen2.write('')
                    if geracao == 'Gen 3':
                        if 'Ruby' in key or 'Saphirre' in key or 'Emerald' in key or 'Firered' in key or 'Leafgreen' in key:
                            st.markdown(''.join(pkdx_entry))
                            col1gen3, col2gen3, col3gen3, col4gen3, col5gen3 = st.columns(5)
                            col1gen3.write('')
                            col2gen3.write('')
                            with col3gen3:
                                st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            with col4gen3:
                                pass
                            with col5gen3:
                                pass
                    if geracao == 'Gen 4':
                        if 'Diamond' in key or 'Pearl' in key or 'Platinum' in key or 'Heartgold' in key or 'Soulsilver' in key:
                            st.markdown(''.join(pkdx_entry))
                            col1gen4, col2gen4, col3gen4, col4gen4, col5gen4 = st.columns(5)
                            with col1gen4:
                                pass
                            with col2gen4:
                                pass
                            with col3gen4:
                                st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            with col4gen4:
                                pass
                            with col5gen4:
                                pass
                    if geracao == 'Gen 5':
                        if 'Black' in key or 'White' in key or 'Black-2' in key or 'White-2' in key:
                            st.markdown(''.join(pkdx_entry))
                            col1gen5, col2gen5, col3gen5, col4gen5, col5gen5 = st.columns(5)
                            with col1gen5:
                                pass
                            with col2gen5:
                                pass
                            with col3gen5:
                                st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            with col4gen5:
                                pass
                            with col5gen5:
                                pass
                    if geracao == 'Gen 6':
                        if 'X' in key or 'Y' in key or 'Omega-ruby' in key or 'Alpha-sapphire' in key:
                            if key == 'Yellow':
                                pass
                            else:
                                st.markdown(''.join(pkdx_entry))
                            col1gen6, col2gen6, col3gen6, col4gen6, col5gen6 = st.columns(5)
                            with col1gen6:
                                pass
                            with col2gen6:
                                pass
                            with col3gen6:
                                if key == 'Yellow':
                                    pass
                                else:
                                    st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            with col4gen6:
                                pass
                            with col5gen6:
                                pass
                    if geracao == 'Gen 7':
                        if 'Sun' in key or 'Moon' in key or 'Ultra-sun' in key or 'Ultra-moon' in key or 'Lets-go-pikachu' in key or 'Lets-go-eevee' in key:
                            st.markdown(''.join(pkdx_entry))
                            col1gen7, col2gen7, col3gen7, col4gen7, col5gen7 = st.columns(5)
                            with col1gen7:
                                pass
                            with col2gen7:
                                pass
                            with col3gen7:
                                st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            with col4gen7:
                                pass
                            with col5gen7:
                                pass
                    if geracao == 'Gen 8':
                        if 'Sword' in key or 'Shield' in key:
                            st.markdown(''.join(pkdx_entry))
                            col1gen8, col2gen8, col3gen8, col4gen8, col5gen8 = st.columns(5)
                            with col1gen8:
                                pass
                            with col2gen8:
                                pass
                            with col3gen8:
                                if pokemon > 809:
                                    st.markdown(f"![SwShSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/{pokemon}.png)")
                                else:
                                    st.markdown(f"![SUMOSprite](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/{pokemon}.png)")
                            with col4gen8:
                                pass
                            with col5gen8:
                                pass

            st.write('***')

            # Imprimindo dados de batalha, tudo feito pegando dados do dataset.
            st.header('Dados de Batalha')
            for c in range(31, 49):
                weakness_append = (tabela2_num[pokemon - 1][c])
                weakness.append(weakness_append)
                weakness_append *= 0
            col1battle, col2battle = st.columns(2)
            with col1battle:
                st.markdown("""###### Recebe Dano Super Efetivo de:""")
                weakness_pokemon = pd.DataFrame(data=weakness, columns=['× DANO'], index=weakness_names)
                st.dataframe(weakness_pokemon)
            with col2battle:
                st.markdown("""###### Valores de Batalha Base""")
                stats = [f'HP : {tabela2_num[pokemon - 1][16]}', f'Ataque : {tabela2_num[pokemon - 1][17]}',
                         f'Defesa : {tabela2_num[pokemon - 1][18]}', f'Ataque Especial : {tabela2_num[pokemon - 1][19]}',
                         f'Defesa Especial : {tabela2_num[pokemon - 1][20]}',
                         f'Velocidade : {tabela2_num[pokemon - 1][21]}']
                stats_num = [tabela2_num[pokemon - 1][16], tabela2_num[pokemon - 1][17], tabela2_num[pokemon - 1][18],
                             tabela2_num[pokemon - 1][19], tabela2_num[pokemon - 1][20], tabela2_num[pokemon - 1][21]]
                stats_color = ['green', 'red', 'grey', 'orange', 'yellow', 'blue', 'black']
                plt.barh(stats, stats_num, 0.5, color=stats_color)
                plt.gca().invert_yaxis()
                plt.show()
                st.pyplot(plt)
                st.write(f'- Total dos valores de batalha : {tabela2_num[pokemon - 1][15]:.0f}')
                st.write(f'- Chance de captura : {tabela2_num[pokemon - 1][22]:.0f}')
                st.write(f'- Taxa de crescimento : {tabela2_num[pokemon - 1][25]}')
                st.write(f'- XP base : {tabela2_num[pokemon - 1][24]:.0f}')

            if geracao == 'Gen 1':
                st.write('')
            else:
                st.write('***')
                # Mais alguns dados do dataset sobre procriação
                st.header('Dados de procriação')
                col1egg, col2egg = st.columns(2)
                with col1egg:
                    if pokemon == 490:
                        st.markdown(f"![ManaphyEgg](https://static.wikia.nocookie.net/pokemon/images/1/14/Manaphy_Egg.png)")
                    else:
                        st.markdown(
                            f"![Egg](https://toppng.com/public/uploads/thumbnail/pokemon-go-egg-11550719099typtypabry.png)")
                with col2egg:
                    st.write('')
                    st.write(f'- Ciclos de ovo : {tabela2_num[pokemon - 1][30]:.0f} ciclos')
                    st.write(f'- Felicidade base : {tabela2_num[pokemon - 1][23]:.0f}')
                    if pd.isnull(tabela2_num[pokemon - 1][29]) == True:
                        st.write(f'- Tipo de ovo : {tabela2_num[pokemon - 1][27]}')
                    else:
                        st.write(f'- Tipo de ovo : {tabela2_num[pokemon - 1][27]} / {tabela2_num[pokemon - 1][28]}')
            st.write('***')

            # Pegando links para sprites do mesmo site que peguei o API, mas ao invés de usar arquivos
            # JSON, estou usando links disponibilizados para cada Pokémon
            st.header('Sprites / Modelos 3D')
            if geracao == 'Gen 1':
                st.write('')
                st.markdown("""##### Pokémon Red / Blue""")
                col1RedBlue, col2RedBlue = st.columns(2)
                with col1RedBlue:
                    st.markdown("""###### Visão frontal""")
                    st.markdown(
                        f"![RedBlueFront](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/{pokemon}.png)")
                with col2RedBlue:
                    st.markdown("""###### Visão Traseiro""")
                    st.markdown(
                        f"![RedBlueBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/{pokemon}.png)")
                st.write('')
                st.markdown("""##### Pokémon Yellow""")
                col1Yellow, col2Yellow = st.columns(2)
                with col1Yellow:
                    st.markdown("""###### Visão Frontal""")
                    st.markdown(
                        f"![YellowFront](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/gray/{pokemon}.png)")
                with col2Yellow:
                    st.markdown("""###### Visão Traseiro""")
                    st.markdown(
                        f"![YellowBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/gray/{pokemon}.png)")
            elif geracao == 'Gen 2':
                st.write('')
                st.markdown("""##### Pokémon Gold""")
                col1Gold, col2Gold = st.columns(2)
                with col1Gold:
                    st.markdown("""###### Visão Frontal""")
                    st.write('- Normal')
                    st.markdown(
                        f"![Gold](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![GoldShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/shiny/{pokemon}.png)")
                with col2Gold:
                    st.markdown("""###### Visão Traseiro""")
                    st.write('- Normal')
                    st.markdown(
                        f"![GoldBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![GoldShinyBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/shiny/{pokemon}.png)")
                st.write('')
                st.markdown("""##### Pokémon Silver""")
                col1Silver, col2Silver = st.columns(2)
                with col1Silver:
                    st.markdown("""###### Visão Frontal""")
                    st.write('- Normal')
                    st.markdown(
                        f"![Silver](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![SilverShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/shiny/{pokemon}.png)")
                with col2Silver:
                    st.markdown("""###### Visão Traseiro""")
                    st.write('- Normal')
                    st.markdown(
                        f"![SilverBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![SilverShinyBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/shiny/{pokemon}.png)")
                st.write('')
                st.markdown("""##### Pokémon Crystal""")
                col1Crystal, col2Crystal = st.columns(2)
                with col1Crystal:
                    st.markdown("""###### Visão Frontal""")
                    st.write('- Normal')
                    st.markdown(
                        f"![Crystal](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![CrystalrShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/shiny/{pokemon}.png)")
                with col2Crystal:
                    st.markdown("""###### Visão Traseiro""")
                    st.write('- Normal')
                    st.markdown(
                        f"![CrystalBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![CrystalShinyBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/shiny/{pokemon}.png)")
            elif geracao == 'Gen 3':
                st.write('')
                st.markdown("""##### Pokémon Ruby / Sapphire""")
                col1RS, col2RS = st.columns(2)
                with col1RS:
                    st.markdown("""###### Visão Frontal""")
                    st.write('- Normal')
                    st.markdown(
                        f"![RuSa](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![RuSaShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/shiny/{pokemon}.png)")
                with col2RS:
                    st.markdown("""###### Visão Traseiro""")
                    st.write('- Normal')
                    st.markdown(
                        f"![RuSaBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![RuSaShinyBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/shiny/{pokemon}.png)")
                st.write('')
                st.markdown("""##### Pokémon Emerald""")
                col1E, col2E = st.columns(2)
                with col1E:
                    st.markdown("""###### Visão Frontal""")
                    st.write('- Normal')
                    st.markdown(
                        f"![Emerald](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![EmeraldShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/shiny/{pokemon}.png)")
                with col2E:
                    st.markdown("""###### Visão Traseiro""")
                    st.write('- Normal')
                    st.markdown(
                        f"![EmeraldBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/{pokemon}.png)")
                    st.write('- Shiny')
                    st.markdown(
                        f"![EmeraldShinyBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/shiny/{pokemon}.png)")
                st.write('')
                st.markdown("""##### Pokémon Fire Red / Leaf Green""")
                col1FRLE, col2FRLE = st.columns(2)
                with col1FRLE:
                    st.markdown("""###### Visão Frontal""")
                    st.write('- Normal')
                    if pokemon < 152:
                        st.markdown(
                            f"![FRLG](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/{pokemon}.png)")
                    else:
                        st.markdown(
                            f"![Emerald](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/{pokemon}.png)")
                    st.write('- Shiny')
                    if pokemon < 152:
                        st.markdown(
                            f"![FRLGShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/shiny/{pokemon}.png)")
                    else:
                        st.markdown(
                            f"![EmeraldShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/shiny/{pokemon}.png)")
                with col2FRLE:
                    st.markdown("""###### Visão Traseiro""")
                    st.write('- Normal')
                    if pokemon < 152:
                        st.markdown(
                            f"![FRLGBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/{pokemon}.png)")
                    else:
                        st.markdown(
                            f"![EmeraldBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/{pokemon}.png)")
                    st.write('- Shiny')
                    if pokemon < 152:
                        st.markdown(
                            f"![FRLGShinyBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/shiny/{pokemon}.png)")
                    else:
                        st.markdown(
                            f"![EmeraldShinyBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/shiny/{pokemon}.png)")
            elif geracao == 'Gen 4':
                st.write('')
                st.markdown("""##### Pokémon Diamond/Pearl""")
                col1DP, col2DP, col3DP, col4DP = st.columns(4)
                with col1DP:
                    if masculino == 0:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.write(
                            f"![DP-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![DPShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/{pokemon}.png)")
                    else:
                        st.markdown("""###### Visão Frontal ♂""")
                        st.write('- Normal')
                        st.write(
                            f"![DP-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![DPShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/{pokemon}.png)")
                with col2DP:
                    if masculino == 0:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![DPBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![DPBackShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/{pokemon}.png)")
                    else:
                        st.markdown("""###### Visão Traseiro ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![DPBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![DPBackShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/{pokemon}.png)")
                with col3DP:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/female/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/female/{pokemon}.png)")
                with col4DP:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/female/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/female/{pokemon}.png)")
                st.write('')
                st.markdown("""##### Pokémon Platinum""")
                col1Plat, col2Plat, col3Plat, col4Plat = st.columns(4)
                with col1Plat:
                    if masculino == 0:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Plat-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![PlatShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/{pokemon}.png)")
                    else:
                        st.markdown("""###### Visão Frontal ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Plat-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![PlatShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/{pokemon}.png)")
                with col2Plat:
                    if masculino == 0:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![PlatBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![PlatBackShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/{pokemon}.png)")
                    else:
                        st.markdown("""###### Visão Traseiro ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![PlatBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![PlatBackShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/{pokemon}.png)")
                with col3Plat:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/female/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/female/{pokemon}.png)")
                with col4Plat:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/female/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/female/{pokemon}.png)")
                st.write('')
                st.markdown("""##### Pokémon HeartGold / SoulSilver""")
                col1HGSS, col2HGSS, col3HGSS, col4HGSS = st.columns(4)
                with col1HGSS:
                    if masculino == 0:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![HGSS-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![HGSSShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/{pokemon}.png)")
                    else:
                        st.markdown("""###### Visão Frontal ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![HGSS-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![HGSSShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/{pokemon}.png)")
                with col2HGSS:
                    if masculino == 0:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![HGSSBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![HGSSBackShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/{pokemon}.png)")
                    else:
                        st.markdown("""###### Visão Traseiro ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![HGSSBack](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![HGSSBackShiny](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/{pokemon}.png)")
                with col3HGSS:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/female/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/female/{pokemon}.png)")
                with col4HGSS:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/female/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/female/{pokemon}.png)")
            elif geracao == 'Gen 5':
                st.write('')
                st.markdown("""##### Pokémon Black / White / Black 2 / White 2""")
                col1BW, col2BW, col3BW, col4BW = st.columns(4)
                with col1BW:
                    if masculino == 0:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![BW-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{pokemon}.gif)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![BWShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/{pokemon}.gif)")
                    else:
                        st.markdown("""###### Visão Frontal ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![BW-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/{pokemon}.gif)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![BWShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/{pokemon}.gif)")
                with col2BW:
                    if masculino == 0:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![BWBack-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/{pokemon}.gif)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![BWShinyBack-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/{pokemon}.gif)")
                    else:
                        st.markdown("""###### Visão Traseiro ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![BWBack-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/{pokemon}.gif)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![BWShinyBack-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/{pokemon}.gif)")
                with col3BW:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Frontal ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/female/{pokemon}.gif)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/female/{pokemon}.gif)")
                with col4BW:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Visão Traseiro ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/female/{pokemon}.gif)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe sprite traseiro fêmea dessa espécie.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/female/{pokemon}.gif)")
            elif geracao == 'Gen 6' or geracao == 'Gen 7':
                st.write('')
                if geracao == 'Gen 6':
                    st.markdown("""##### Pokémon X / Y / Omega Ruby / Alpha Saphirre""")
                elif geracao == 'Gen 7':
                    st.markdown("""##### Pokémon Sun / Moon / Ultra Sun / Ultra Moon""")
                elif geracao == 'Gen 8':
                    st.markdown("""##### Pokemon Sword / Shield""")
                col13D, col23D = st.columns(2)
                with col13D:
                    if masculino == 0:
                        st.markdown("""###### Modelo 3D do Pokémon ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![3D-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![3DShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/{pokemon}.png)")
                    else:
                        st.markdown("""###### Modelo 3D do Pokémon ♂""")
                        st.write('- Normal')
                        st.markdown(
                            f"![3D-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![3DShiny-M](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/{pokemon}.png)")
                with col23D:
                    if masculino == 100 or masculino == 0:
                        pass
                    else:
                        st.markdown("""###### Modelo 3D do Pokémon ♀""")
                        st.write('- Normal')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/female/{pokemon}.png)")
                        st.write('- Shiny')
                        st.markdown(
                            f"![Não existe diferencial entre macho e fêmea desse pokémon.](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/female/{pokemon}.png)")
            elif geracao == 'Gen 8':
                st.subheader('- Não tem dados dos sprites dos Pokémons da oitava geração.')

if menu == 'Dados dos Ataques':
    tabelamoves = pd.read_csv('pokemon_dataset/All_Moves.csv')
    st.sidebar.title('Filtragem de Ataques')
    filtragem = st.sidebar.checkbox('Clique para pesquisar ataques específicos.')
    # Pesquisando por um ataque espécifico
    if filtragem:
        ataque_nome = st.sidebar.text_input('Escreva o nome dos ataques: ', value='').title().strip()
        for c in range(0, len(tabelamoves)):
            if ataque_nome == tabelamoves.iloc[c].iloc[0]:
                st.title(ataque_nome)
                col1move, col2move, col3move = st.columns(3)
                with col1move:
                    st.markdown('***')
                    st.markdown('#### Descrição do Ataque')
                    st.write('')
                    st.write('')
                    st.write(f'###### - {tabelamoves.iloc[c].iloc[3]}')
                with col2move:
                    st.write('***')
                    st.markdown('##### Tipo Elemental do Ataque')
                    if tabelamoves.iloc[c].iloc[1] == 'Normal':
                        st.markdown(f'- ![Normal](https://archives.bulbagarden.net/media/upload/8/89/NormalIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Fighting':
                        st.markdown(f'- ![Fighting](https://archives.bulbagarden.net/media/upload/3/35/FightingIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Flying':
                        st.markdown(f'- ![Flying](https://archives.bulbagarden.net/media/upload/0/03/FlyingIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Poison':
                        st.markdown(f'- ![Poison](https://archives.bulbagarden.net/media/upload/8/8b/PoisonIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Ground':
                        st.markdown(f'!- [Ground](https://archives.bulbagarden.net/media/upload/b/bd/GroundIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Rock':
                        st.markdown(f'!- [Rock](https://archives.bulbagarden.net/media/upload/9/98/RockIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Bug':
                        st.markdown(f'- ![Bug](https://archives.bulbagarden.net/media/upload/9/9c/BugIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Ghost':
                        st.markdown(f'- ![Ghost](https://archives.bulbagarden.net/media/upload/4/45/GhostIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Steel':
                        st.markdown(f'- ![Steel](https://archives.bulbagarden.net/media/upload/5/5f/SteelIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Fire':
                        st.markdown(f'- ![Fire](https://archives.bulbagarden.net/media/upload/b/b1/FireIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Water':
                        st.markdown(f'- ![Water](https://archives.bulbagarden.net/media/upload/2/2b/WaterIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Grass':
                        st.markdown(f'- ![Grass](https://archives.bulbagarden.net/media/upload/a/ad/GrassIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Electric':
                        st.markdown(f'- ![Electric](https://archives.bulbagarden.net/media/upload/b/b4/ElectricIC_LA.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Psychic':
                        st.markdown(f'- ![Psychic](https://archives.bulbagarden.net/media/upload/6/68/PsychicIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Ice':
                        st.markdown(f'- ![Ice](https://archives.bulbagarden.net/media/upload/1/11/IceIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Dragon':
                        st.markdown(f'- ![Dragon](https://archives.bulbagarden.net/media/upload/c/c7/DragonIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Dark':
                        st.markdown(f'- ![Dark](https://archives.bulbagarden.net/media/upload/b/b9/DarkIC_BDSP.png)')
                    elif tabelamoves.iloc[c].iloc[1] == 'Fairy':
                        st.markdown(f'- ![Fairy](https://archives.bulbagarden.net/media/upload/d/d6/FairyIC_BDSP.png)')
                    else:
                        st.write(tabelamoves.iloc[c].iloc[1])
                    st.write('')
                    st.write('***')
                    st.markdown('##### Poder do Ataque')
                    st.markdown(f'- {tabelamoves.iloc[c].iloc[4]}')
                    st.write('')
                    st.markdown('***')
                    st.markdown('##### Power Points (PP)')
                    st.markdown(f'- {tabelamoves.iloc[c].iloc[6]}')
                with col3move:
                    st.write('***')
                    st.markdown('##### Categoria de Dano do Ataque')
                    if tabelamoves.iloc[c].iloc[2] == 'Physical':
                        st.markdown(f'- ![Physical](https://oyster.ignimgs.com/mediawiki/apis.ign.com/pokemon-switch/e/ef/Physical.png?width=325)')
                    if tabelamoves.iloc[c].iloc[2] == 'Special':
                        st.markdown(f'- ![Special](https://oyster.ignimgs.com/mediawiki/apis.ign.com/pokemon-switch/2/24/Special.png?width=325)')
                    if tabelamoves.iloc[c].iloc[2] == 'Status':
                        st.markdown(f'- ![Status](https://oyster.ignimgs.com/mediawiki/apis.ign.com/pokemon-switch/d/d0/Status.png?width=325)')
                    st.markdown('***')
                    st.markdown('##### Acurácia')
                    st.markdown(f'- {tabelamoves.iloc[c].iloc[5]}')
                    st.write('')
                    st.markdown('***')
                    st.markdown('##### Probabilidade de Efeito Adicional')
                    st.markdown(f'- % {tabelamoves.iloc[c].iloc[8]}')

    # Olhando todos os ataques dos jogos
    else:
        page = st.sidebar.selectbox(
            'Página',
            ('Página 1', 'Página 2', 'Página 3', 'Página 4', 'Página 5'))
        st.title('Ataques')
        st.markdown('***')
        col1desc, col2desc, col3desc, col4desc = st.columns(4)
        with col1desc:
            st.markdown('###### Nome')
        with col2desc:
            st.markdown('###### Tipo elemental | Tipo de Ataque')
        with col3desc:
            st.markdown('###### Descrição do ataque')
        with col4desc:
            st.markdown('###### Pwr|Acurácia|PP|Prob.Efct')
        if page == 'Página 1':
            inicio = 0
            fim = 146
        elif page == 'Página 2':
            inicio = 146
            fim = 292
        elif page == 'Página 3':
            inicio = 292
            fim = 438
        elif page == 'Página 4':
            inicio = 438
            fim = 584
        elif page == 'Página 5':
            inicio = 584
            fim = len(tabelamoves)
        else:
            inicio = 0
            fim = 146
        for c in range(inicio, fim):
            col1move, col2move, col3move, col4move = st.columns(4)
            with col1move:
                st.markdown(f'{tabelamoves.iloc[c].iloc[0]}')
            with col2move:
                st.markdown(f'{tabelamoves.iloc[c].iloc[1]} | {tabelamoves.iloc[c].iloc[2]}')
            with col3move:
                st.markdown(f'{tabelamoves.iloc[c].iloc[3]}')
            with col4move:
                if tabelamoves.iloc[c].iloc[4] == '-':
                    st.markdown(f'\{tabelamoves.iloc[c].iloc[4]} | {tabelamoves.iloc[c].iloc[5]} | {tabelamoves.iloc[c].iloc[6]} | {tabelamoves.iloc[c].iloc[8]}')
                else:
                    st.markdown(f'{tabelamoves.iloc[c].iloc[4]} | {tabelamoves.iloc[c].iloc[5]} | {tabelamoves.iloc[c].iloc[6]} | {tabelamoves.iloc[c].iloc[8]}')
