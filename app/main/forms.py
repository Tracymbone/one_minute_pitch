from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField,PasswordField
from wtforms.validators import input_required
categories = ['pickup','interview','product','promotion']


class UpdateForm(FlaskForm):
    biography = TextAreaField("Your Biography", validators=[input_required(message='Biography field is required')],render_kw={"placeholder": "Your Biography"})
    submit = SubmitField("Update Profile")


class PostForm(FlaskForm):
    title = StringField("pitch title", validators=[input_required(message='Pitch title is required')],render_kw={"placeholder":"Pitch Title"})
    category = SelectField("Pitch category", validators=[input_required(message="Pitch Category required")],choices=categories)
    post = TextAreaField("Pitch description", validators=[input_required(message="Pitch required")],render_kw={"placeholder":"Pitch description"})
    submit = SubmitField("Post Pitch")


class CommentForm(FlaskForm):
    comment = TextAreaField('Pitch comment', validators=[input_required(message="Comment field is required")],render_kw={"placeholder": "Your Comment"})
    submit = SubmitField('Comment')