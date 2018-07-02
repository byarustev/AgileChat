from .user import User
# from comment import Comment
# from log import Log
first_prompt = """
please login to use the application
enter username: 
"""

password_prompt = "enter password: "

system_menu = """
Logged in as {0}
1. create a new comment
2. view my comments 
3. view all comment
"""

if __name__ == "__main__":

    username = input(first_prompt)
    if username:
        password = input(password_prompt)

        if User.login(username, password):
            answer = input(system_menu)

            if answer == 1:
                prompt1="Enter comment title"

