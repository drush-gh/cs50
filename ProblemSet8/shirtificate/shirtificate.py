from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margin(0)
    pdf.set_y(25)
    pdf.set_auto_page_break(True)
    pdf.set_font("Courier", size=48, style="B")
    pdf.cell(text="CS50 Shirtificate", center=True, align="X")
    pdf.image("shirtificate.png", h=(pdf.eph/2 + 50), w=(pdf.eph/2 + 50), x=(pdf.eph/8 - 30), y=(pdf.eph/8 + 25))
    pdf.set_xy(x=pdf.eph/4, y=(pdf.eph/4 + 50))
    pdf.set_font("Courier", size=24, style="B")
    pdf.set_text_color(255,255,255)
    pdf.cell(text=f"{name} took CS50", center=True, align="X")


    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
