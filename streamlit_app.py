import streamlit as st
import cosine_comparator
from styles.styles import get_color_by_value, get_style, get_winner_style


def handle_chat_input(prompt):
    points = cosine_comparator.get_score(prompt)
    if(points == 10000):
        print_winner(prompt)
    else:
        score = (prompt, points)
        st.session_state.scores.append(score)
        st.session_state.scores.sort(key=lambda x: x[1], reverse=True)
    print_all_messages(st.session_state.scores)

def print_winner(text):
    estilo_css = get_winner_style()

    st.markdown(estilo_css, unsafe_allow_html=True)
    st.markdown(f'<div class="my-box">{text.upper()}</div>'
                '</div>', unsafe_allow_html=True)

def print_all_messages(pares):
    estilo_css = get_style()

    st.markdown(estilo_css, unsafe_allow_html=True)
    for par in pares:
        color , background_color= get_color_by_value(par[1])
        st.markdown(f'<div class="my-box" style="border: 2px solid {color}; background-color: {background_color};">'
                f'<div class="column">{str(par[0])}</div>'
                f'<div class="column">{str(par[1])}</div>'
                '</div>', unsafe_allow_html=True)


 


def main():



    st.header("Adivina la palabra")

    
    if "scores" not in st.session_state:
        st.session_state.scores = []
    
    with st.sidebar:

        st.subheader("Estemos en contacto:")

        linkedin_logo = "social_logos/LI-In-Bug.png"
        st.image(linkedin_logo, width=16, use_column_width=False)
        st.markdown(f"[@lucasbiagettia](https://www.linkedin.com/in/lucasbiagettia/)")

        github_logo = "social_logos/github-mark.png"
        st.image(github_logo, width=16, use_column_width=False)
        st.markdown(f"[@lucasbiagettia](https://github.com/lucasbiagettia/)")

        hugging_face_logo = "social_logos/hf-logo.png"
        st.image(hugging_face_logo, width=16, use_column_width=False)
        st.markdown(f"[@lucasbiagettia](https://huggingface.co/lucasbiagettia)")


  


    prompt = st.chat_input("Escribe una palabra")
    if prompt:
        handle_chat_input(prompt)


if __name__ == "__main__":
    main()
