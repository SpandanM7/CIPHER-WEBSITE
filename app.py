import streamlit as st
import random

class decore:
    def __init__(self, key):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.!? "
        self.key = key

    def decode(self, encoded_message):
        decoded_message = ''.join([self.alphabet[self.key.find(char)] for char in encoded_message])
        return decoded_message

class encore:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.!? "
        self.shuffle_alphabet()

    def shuffle_alphabet(self):
        random.seed(42) 
        self.key = list(self.alphabet)
        random.shuffle(self.key)
        self.key = ''.join(self.key)

    def encode(self, message):
        encoded_message = ''.join([self.key[self.alphabet.find(char)] for char in message])
        return encoded_message


def blink_text(text, blink_count=1):
    for _ in range(blink_count):
        st.markdown(f"<div class='blink-text'>{text}</div>", unsafe_allow_html=True)



st.markdown(
    """
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    .blink-text {
        animation: blink 1s infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def home_page():
    st.title("A SIMPLE CIPHER")
    blink_text("There's a dropdown menu on the left, choose according to your needs.")
'''
def about_page():
    st.title("About Me")
    st.write("Spandan Mukherjee from Kolkata, India - where every moment is a canvas (It most certaily is not :skull:). \nCurrently a sophomore at TINT Newtown. ")
    img_path="img.jpg"
    st.image(img_path, caption="Don't I look hot?", width=600)
    ins_img="insta.jpg"
    # ins_url="https://www.instagram.com/spanda___n?igshid=ODA1NTc5OTg5Nw=="
    st.image(ins_img, width=20)
    st.markdown("[Instagram](https://www.instagram.com/spanda___n?igshid=ODA1NTc5OTg5Nw==)")


'''
#encryption
def encryp():
    st.title("Encryption")
    message_to_encode = st.text_input("Enter your message to encrypt: ")
    button1=st.button("submit")
    if button1:
        if (message_to_encode != ""):
            cipher = encore()
            st.write("Encoded message: ")
            encoded_message = cipher.encode(message_to_encode)
            st.write(encoded_message)
            # st.write("Key: ")
            # st.write(cipher.key)  
        else:
            st.text("PLEASE INSERT SOMETHING.")

    
#decryption
def decryp():
    st.title("Decryption")
    message_to_decode = st.text_input("Enter your encoded message to decrypt: ")
    button2=st.button("submit")
    if button2:
        if (message_to_decode != ""):
            sect="PxdZH5s.QyJheUSuXnt9TWLo60?qY7EkV1KAR2cwa4pM!zmg,N3BCblFi8rGvI fjDO"
            decoded_cipher = decore(sect)
            decoded_message = decoded_cipher.decode(message_to_decode)
            st.write("Decoded message: ")
            st.write(decoded_message)
        else:
            st.text("PLEASE INSERT SOMETHING.")
        

def main():
    page = st.sidebar.selectbox("Select a page", ["Home", "About Me", "Encryption","Decryption"])

    if page == "Home":
        home_page()
    '''
    elif page == "About Me":
        about_page()
    '''
    elif page =="Encryption":
        encryp()
    elif page == "Decryption":
        decryp()

if __name__ == "__main__":
    main()
    
