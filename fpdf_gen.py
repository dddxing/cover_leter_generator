from fpdf import FPDF
import config
# from main import position, company, _type


class PDF:

    pdf = FPDF("P", 'mm', "Letter")

    pdf.add_page()

    # Set auto page break
    pdf.set_auto_page_break(auto=True, margin=15)

    name = "Daming Xing"
    greeting = "Dear Hiring Team,"
    header = "421 W 118th Street #61B, New York, NY 10027 | " \
             "daming.xing@columbia.edu | daming-xing.com | " \
             "(860)978-8687"

    # p = config.position
    # c = config.company
    # t = config.type_


    # intro_para = f"I am writing to express my interest in the {p} role at {c}. " \
    #              f"Currently, I am pursuing my " \
    #              f"Master of Science in Mechanical Engineering (Robotics & Control Track) at Columbia University. " \
    #              f"Before joining Columbia, I worked as an Automation Engineer at Stanley Black & Decker's Industry " \
    #              f"4.0 team. I believe my education and previous work experiences in {t} are an excellent match " \
    #              f"with the responsibilities outlined in the job description."

    robotics_para = "Prior to joining Stanley Black & Decker, I was heavily involved in robotics research at Trinity " \
                    "College (Hartford, CT). My research paper, titled 'An Intelligent Sensor-Driven Skydive " \
                    "Tracking System', presented a near-real-time error-correction and sensor consolidation " \
                    "method for skydive tracking systems to prevent aviation mishaps and fatalities. " \
                    "After graduating with a BS degree in Engineering from Trinity College, " \
                    "I worked as an Automation Engineer at Stanley Black & Decker's Industry 4.0 team for almost 3 " \
                    "years, working on advanced automation and robotics technologies. Being the Subject-Matter " \
                    "Expert (SME) in Autonomous Mobile Robot (AMR) at Stanley Black & Decker, I established an " \
                    "ecosystem for AMR projects from the discovery to the deployment stage, slashing time " \
                    "to deploy by 67%+."

    # last_para = f"My experience at Columbia University and Stanley Black & Decker has prepared me to contribute to " \
    #             f"the {t} team at {c} immediately. I would be grateful for " \
    #             f"the opportunity to speak with you regarding the {p}. Please feel free to contact me if any " \
    #             f"additional information I could provide would assist you in evaluating my application. "

    signature_para = "Sincerely,"

    def _add_paragraph(self, paragraph_name):
        self.pdf.set_font('times', '', 12)
        self.pdf.cell(-200)
        self.pdf.ln(5)
        self.pdf.multi_cell(w=197, h=7, txt=paragraph_name, border=0, align='L')

    def intro_para(self, p, c, t):
        intro_para = f"I am writing to express my interest in the {p} role at {c}. " \
                     f"Currently, I am pursuing my " \
                     f"Master of Science in Mechanical Engineering (Robotics & Control Track) at Columbia University. " \
                     f"Before joining Columbia, I worked as an Automation Engineer at Stanley Black & Decker's Industry " \
                     f"4.0 team. I believe my education and previous work experiences in {t} are an excellent match " \
                     f"with the responsibilities outlined in the job description."
        self._add_paragraph(intro_para)

    def last_para(self, p, c, t):
        last_para = f"My experience at Columbia University and Stanley Black & Decker has prepared me to contribute to " \
                f"the {t} team at {c} immediately. I would be grateful for " \
                f"the opportunity to speak with you regarding the {p}. Please feel free to contact me if any " \
                f"additional information I could provide would assist you in evaluating my application. "

        self._add_paragraph(last_para)

    def create_header(self):
        # pdf.set_font('times', 'B', 20)
        self.pdf.ln(7)

        self.pdf.set_font('times', 'B', 20)
        self.pdf.cell(w=197, h=7, txt=self.name, align='C', ln=1)
        self.pdf.ln(2)

        self.pdf.line(10, 33, 205, 33)
        self.pdf.set_font('times', '', 12)
        self.pdf.cell(w=197, h=7, txt=self.header, align='C')
        self.pdf.ln(15)

    def create_body(self, position, company, type_):
        self._add_paragraph(self.greeting)

        self.intro_para(position, company, type_)
        self._add_paragraph(self.robotics_para)
        self.last_para(position, company, type_)
        self._add_paragraph(self.signature_para)
        self._add_paragraph(self.name)

    def save_pdf(self, loc):
        self.pdf.output(loc, 'F')

    def create_cover_letter(self, loc, p, c, t):
        self.create_header()
        self.create_body(p, c, t)
        self.save_pdf(loc)
        return True


def main():
    p = PDF()
    p.create_cover_letter("test.pdf", "POSITION", "COMPANY", "TYPE")


if __name__ == "__main__":
    main()





