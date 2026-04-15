client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Get Product Name and Audience for That Product
product = st.text_input("Product")
audience = st.text_input("Audience")

# Button to Generate Content
if st.button("Generate Content"):
    prompt = f"Write marketing content for {product} targeting {audience}."
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    st.session_state.text = response.choices[0].message.content
