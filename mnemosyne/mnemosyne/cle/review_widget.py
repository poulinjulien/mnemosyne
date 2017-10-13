#
# review_wdgt.py <Peter.Bienstman@UGent.be>
#

from mnemosyne.libmnemosyne.ui_components.review_widget import ReviewWidget


class ReviewWdgt(ReviewWidget):

    def redraw_now(self):
        pass

    def empty(self):
        background = "white"
        if self.review_controller().card:
            colour = self.config().card_type_property(\
            "background_colour", self.review_controller().card.card_type)
            if colour:
                background = ("%X" % colour)[2:] # Strip alpha.
        return """
        <html><head>
        <style type="text/css">
        table { height: 100%; }
        body  { background-color: """ + background + """;
                margin: 0;
                padding: 0;
                border: thin solid #8F8F8F; }
        </style></head>
        <body><table><tr><td>
        </td></tr></table></body></html>"""

    def show_answer(self):
        self.review_controller().show_answer()

    def grade_answer(self, grade):
        self.review_controller().grade_answer(grade)

    def set_question_box_visible(self, is_visible):
        self.component_manager.android.setQuestionBoxVisible(is_visible)

    def set_answer_box_visible(self, is_visible):
        self.component_manager.android.setAnswerBoxVisible(is_visible)

    def set_question_label(self, text):
        self.component_manager.android.setQuestionLabel(text.encode("utf-8"))

    def set_question(self, text):
        self.question = text

    def set_answer(self, text):
        self.answer = text

    def reveal_question(self):
        print("Q:", self.question.encode("utf-8"))
        self.component_manager.android.setQuestion(\
            self.question.encode("utf-8"))

    def reveal_answer(self, process_audio=True):
        print("A:", self.answer.encode("utf-8"))
        self.component_manager.android.setAnswer(\
            self.answer.encode("utf-8"), process_audio)

    def clear_question(self):
        self.question = self.empty()
        self.reveal_question()

    def clear_answer(self):
        # We don't process the audio here, as that would kill the pending
        # audio events from the question.
        self.answer = self.empty()
        self.reveal_answer(process_audio=False)

    def update_show_button(self, text, is_default, is_enabled):
        self.component_manager.android.updateShowButton(\
            text.encode("utf-8"), is_default, is_enabled)

    def set_grades_enabled(self, is_enabled):
        self.component_manager.android.setGradesEnabled(is_enabled)

    def set_default_grade(self, grade):
        pass

    def update_status_bar_counters(self):
        scheduled_count, non_memorised_count, active_count = \
            self.review_controller().counters()
        counters = "Sch.: %d Not mem.: %d Act.: %d" % \
                    (scheduled_count, non_memorised_count, active_count)
        self.component_manager.android.setStatusbarText(counters)

