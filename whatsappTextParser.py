from objection_engine.beans.comment import Comment
import objection_engine

class Message:
    text: str = None
    UserID = None

    def to_message(self):
        return Comment(text_content=self.text, user_id=self.UserID, user_name=self.UserID, evidence_path=None)

def parseMessage(line: str) -> Comment:
    result: Message = Message()
    result.text = line.split(':',2)[-1][1:-1]
    result.UserID = line.split(':',2)[1].split(' ', 2)[-1]
    return result.to_message()

def parseMessages(fileName: str) -> [Comment]:
    result: [Comment] = []
    f = open(fileName, "r")
    for line in f:
        result.append(parseMessage(line))
    print(result)
    return result

def createVideo(convo: [Comment]):
        thread = convo
        # Thread is populated
        output_filename = 'output8.mp4'
        objection_engine.renderer.render_comment_list(thread, output_filename=output_filename)
