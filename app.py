import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="NOGD3V", page_icon=":globe_with_meridians:")


with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

#Função para importar os dados da animação:

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Importando animação
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_dews3j6m.json")
lottie_coding2 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
#Barra lateral
st.sidebar.title('Seja bem-vindo(a)')

#Select box dentro da barra lateral
paginaselecionada = st.sidebar.selectbox('Navegue pelas paginas escrevendo ↓', ['Home', 'Dia a Dia'])

if paginaselecionada == 'Home':
    with st.container():
        st.subheader("Olá, me chamo Lucas :wave:")
        st.title("O melhor engenheiro de dados do meu bairro :infinity:")
        st.write("##")
        st.write("Apaixonado pela área de dados, extraio, carrego e transformo dados para solucionar problemas empresáriais.")
        st.write("[Visite meu LINKEDIN > ](https://www.linkedin.com/in/nogd3v/)")
        st_lottie(lottie_coding2, height=400, key="coding")

if paginaselecionada == 'Dia a Dia':
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Meu dia a dia (tools)")
            st.write("##")
            st.write(
                """
                Atualmente essas são as minhas competencias para solucionar problemas:
                Competências: iceberg · Integração e entrega contínuas (CI/CD) · Minio · Trino · Kubernetes · Apache Airflow · Bitbucket · ETL (Extração, transformação e carregamento) · Tunning · Administrador de banco de dados · Monitoramento de banco de dados · Python · Google Cloud Platform (GCP) · PostgreSQL · Apache Spark · PySpark · Microsoft SQL Server · SSIS · SQL · Transact-SQL · Docker · Linux · Scrum
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=400, key="coding")