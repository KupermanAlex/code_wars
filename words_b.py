def reverse(st):
    """t reverses the words in a given string"""
    st = st.split()
    st.reverse()
    return ' '.join(st)