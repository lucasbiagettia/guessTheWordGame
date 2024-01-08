def get_style():
    return """
        <style>
            body {
                background-color: rgba(0, 0, 255, 0.1); /* Fondo poco opaco azul */
            }
            h1 {
                color: #3366cc;
            }
            .my-box {
                border-radius: 10px;
                padding: 10px;
                margin: 10px 0;
                display: flex;
                flex-direction: row;
                justify-content: center;
                font-size: 34px;
            }
            .column {
                width: 48%;
            }
        </style>
"""
def get_color_by_value(value):
    value = max(0, min(10000, value))
    green_value = int(value / 10000 * 255)
    red_value = 255 - green_value
    color_css = f'rgb({red_value}, {green_value}, 0)'
    color_back_css = f'rgba({red_value}, {green_value}, 0, 0.1)'
    return color_css , color_back_css


