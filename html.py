def get_html(ip):
    return """
<!DOCTYPE html>
<html>
  <head>
    <title>Servo Control</title>
    <style>
      body {
        background-color: blue;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
      }
      .contenedor {
        background-color: white;
        color: black;
        max-width: 400px;
        margin: 80px auto;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0,0,0,0.3);
      }
      input[type=range] {
        width: 100%;
        margin-top: 20px;
      }
    </style>
  </head>
  <body>
    <div class="contenedor">
      <h2>Control de Servo</h2>
      <input type="range" min="0" max="180" value="90" id="slider" oninput="mover(this.value)">
      <p>Ángulo actual: <span id="valor">90</span>°</p>
    </div>

    <script>
      function mover(val) {
        document.getElementById("valor").innerText = val;
        fetch('/servo?g=' + val);
      }
    </script>
  </body>
</html>
"""
