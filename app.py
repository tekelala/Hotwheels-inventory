import streamlit as st
from PIL import Image

# Create a class to hold the car data
class Car:
    def __init__(self, name, year, model, comments, image):
        self.name = name
        self.year = year
        self.model = model
        self.comments = comments
        self.image = image

# Create a list to hold the car objects
cars = []

# Function to display the car data
def display_cars(cars):
    for car in cars:
        st.subheader(car.name)
        st.image(car.image)
        st.text(f"Year: {car.year}")
        st.text(f"Model: {car.model}")
        st.text(f"Comments: {car.comments}")

# Title of the app
st.title("Hot Wheels Inventory Management")

# User can upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# User can input details about the car
name = st.text_input("Name")
year = st.text_input("Year")
model = st.text_input("Model")
comments = st.text_input("Comments")

if st.button('Add Car'):
    new_car = Car(name, year, model, comments, image)
    cars.append(new_car)

# Display the car data
display_cars(cars)
