from comment import Comment
from user import User
from AgileChat import comments

class Moderators(User):
    def __init__(self,moderator_id,moderator_name):
        self.moderator_id = moderator_id
        self.moderator_name = moderator_name
       

    def edit_comments(self,):
        pass
     
             
        
         
      
    def delete_comment(self,comment_id):
        comments.remove(comment_id - 1)
        
        

       
