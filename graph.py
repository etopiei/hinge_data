import plotly.graph_objects as go
import json

match_data = json.loads(open(input("Enter hinge match filename: ")).read())

number_of_likes_sent = sum([1 for person in match_data if "like" in person])
number_of_likes_received = len(match_data) - number_of_likes_sent

total_likes = number_of_likes_sent + number_of_likes_received

matches_from_like_sent = sum([1 for person in match_data if "match" in person and "like" in person])
matches_from_like_receieved = sum([1 for person in match_data if "match" in person and "like" not in person])

reject_from_like_sent = number_of_likes_sent - matches_from_like_sent
reject_from_like_recieved = number_of_likes_received - matches_from_like_receieved

meetups = sum([1 for person in match_data if "we_met" in person])
match_no_meet = matches_from_like_sent + matches_from_like_receieved - meetups

figure = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 4,
        thickness = 6,
        line = dict(color= "black", width = 0.1),
        label = ["Likes", "Like Sent", "Like Received", "No Match", "Matched", "Met Up", "No Meet Up"],
        color = "red"
    ),
    link = dict(
        source = [0, 0, 1, 1, 2, 2, 4, 4], 
        target = [1, 2, 4, 3, 4, 3, 5, 6], 
        value = [number_of_likes_sent, number_of_likes_received, matches_from_like_sent, reject_from_like_sent, matches_from_like_receieved, reject_from_like_recieved, meetups, match_no_meet]
        ))])

figure.update_layout(title_text="Hinge Likes", font_size=12)
figure.show()



