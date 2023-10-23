import streamlit as st

st.set_page_config(
    page_title="Home",
    layout='wide',
    page_icon='./images/home.png'
)

# Add an image banner at the top
banner_image = './images/banner.jpg'
st.image(banner_image, use_column_width=True)

st.title("Welcome to YOLO Object Detection App")
st.caption('This web application demonstrates Object Detection')

# Add interactive buttons for different app sections
col1, col2 = st.columns(2)

with col1:
    if st.button("Object Detection for Images"):
        st.markdown("[Click here for App](/YOLO_for_image/)")
    if st.button("Live Object Detection"):
        st.markdown("[Click here for App](/YOLO_webrtc/)") 
    # Add code to navigate to the respective page

with col2:
    with st.expander("List of Detected Objects"):
        st.markdown("""
        Below are the objects that our model can detect:
        1. Person
        2. Car
        3. Chair
        4. Bottle
        5. Sofa
        6. Bicycle
        7. Horse
        8. Boat
        9. Motor Bike
        10. Cat
        11. Tv Monitor
        12. Cow
        13. Sheep
        14. Aeroplane
        15. Train
        16. Dining Table
        17. Bus
        18. Potted Plant
        19. Bird
        20. Dog
        """
        )
