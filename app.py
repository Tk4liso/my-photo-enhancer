from src.models import ImageEnhancer
from src.utils import pil_to_bgr, bgr_to_pil, load_image
from src.ui import (
    render_header,
    render_file_uploader,
    render_instructions,
    render_interactive_slider,
    render_download_button
)
import streamlit as st
from config import PAGE_CONFIG

st.set_page_config(**PAGE_CONFIG)

def main():
    """Función principal de la aplicación"""

    render_header()
    
    #Inicializar el modelo
    enhacer = ImageEnhancer()
    st.success("Modelos listos")
    
    #Subir fichero
    uploaded_file = render_file_uploader()
    
    if uploaded_file is not None:
        # Cargar imagen
        original_image = load_image(uploaded_file)
        img_bgr = pil_to_bgr(original_image)
        
        #Mostrar imagen original
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original")
            st.image(original_image, width="stretch")
        
        # OPCIONES DE PROCESAMIENTO
        st.markdown("---")
        st.subheader("Opciones de mejora")
        
        col_opt1, col_opt2 = st.columns(2)
        
        with col_opt1:
            reparir_scratches = st.checkbox(
                "Reparar grietas",
                value=False,
                help="Elimina rayas y arañazos de la foto"
            )
            
        with col_opt2:
            enhance_background = st.checkbox(
                "Mejorar calidad de fondo",
                value=False,
                help="Usa RealESGRAN para mejorar el fondo (más lento)"
            )
        
        st.markdown("---")
        
        #Botón de procesamiento
        if st.button("Mejorar calidad", type="primary", width="stretch"):
            with st.spinner("Procesando imagen..."):
                #Mejorar imagen con opciones seleccionadas
                restored_bgr = enhacer.enhance(
                    img_bgr,
                    repair_scratches=reparir_scratches,
                    enhance_background=enhance_background #Para mejorar fondos
                )
                restored_image = bgr_to_pil(restored_bgr)
                
                #Guardar la imagen en session state (estado de sesión de streamlit)
                st.session_state["restored_image"] = restored_image
                st.session_state["original_image"] = original_image
                
                st.success("¡Imagen mejorada!")
                st.rerun()
        
        #Mostrar el resultado si existe
        if 'restored_image' in st.session_state:
            with col2:
                st.subheader("Mejorada")
                st.image(st.session_state['restored_image'], width="stretch")
            
            #Comparador interactivo
            render_interactive_slider(
                st.session_state['original_image'],
                st.session_state['restored_image']
            )
            
            #Botón de descarga
            render_download_button(st.session_state['restored_image'])
    else:
        render_instructions()

# COMANDO PARA CORRER STREAMLIT (en la carpeta de my-photo-enhancer): >streamlit run .\app.py
if __name__ == "__main__":
    main()