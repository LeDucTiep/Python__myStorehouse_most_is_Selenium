import cairosvg

svg_code = """
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="76pt" height="35pt" viewBox="0 0 76 35" version="1.1">
<g id="surface305271">
<rect x="0" y="0" width="76" height="35" style="fill:rgb(0%,0%,0%);fill-opacity:1;stroke:none;"/>
<path style=" stroke:none;fill-rule:nonzero;fill:rgb(100%,100%,100%);fill-opacity:1;" d="M 15.1875 14.523438 L 15.1875 24.820312 L 16.9375 24.820312 L 16.9375 10.367188 L 15.78125 10.367188 C 15.15625 12.585938 14.765625 12.882812 12.046875 13.242188 L 12.046875 14.523438 Z M 31.808594 19.476562 L 27.667969 19.476562 L 27.667969 15.335938 L 26.261719 15.335938 L 26.261719 19.476562 L 22.121094 19.476562 L 22.121094 20.882812 L 26.261719 20.882812 L 26.261719 25.023438 L 27.667969 25.023438 L 27.667969 20.882812 L 31.808594 20.882812 Z M 42.753906 14.117188 C 42.425781 11.757812 40.894531 10.367188 38.738281 10.367188 C 37.175781 10.367188 35.785156 11.117188 34.941406 12.414062 C 34.035156 13.835938 33.660156 15.601562 33.660156 18.226562 C 33.660156 20.664062 34.003906 22.195312 34.863281 23.476562 C 35.613281 24.664062 36.863281 25.273438 38.425781 25.273438 C 41.113281 25.273438 43.066406 23.257812 43.066406 20.445312 C 43.066406 17.773438 41.253906 15.898438 38.722656 15.898438 C 37.316406 15.898438 36.222656 16.414062 35.457031 17.476562 C 35.488281 13.898438 36.597656 11.914062 38.613281 11.914062 C 39.863281 11.914062 40.722656 12.726562 41.003906 14.117188 Z M 38.503906 17.460938 C 40.207031 17.460938 41.253906 18.664062 41.253906 20.585938 C 41.253906 22.398438 40.066406 23.726562 38.441406 23.726562 C 36.800781 23.726562 35.566406 22.335938 35.566406 20.507812 C 35.566406 18.695312 36.753906 17.460938 38.503906 17.460938 Z M 54.609375 17.757812 L 44.921875 17.757812 L 44.921875 19.164062 L 54.609375 19.164062 Z M 54.609375 21.195312 L 44.921875 21.195312 L 44.921875 22.601562 L 54.609375 22.601562 Z M 62.195312 20.835938 L 62.195312 19.898438 C 62.226562 19.007812 62.507812 18.554688 63.789062 17.414062 C 65.289062 16.054688 65.789062 15.179688 65.789062 13.835938 C 65.789062 11.507812 64.117188 10.007812 61.523438 10.007812 C 58.617188 10.007812 57.148438 11.585938 57.148438 14.679688 L 58.835938 14.679688 C 58.835938 12.523438 59.617188 11.554688 61.414062 11.554688 C 62.960938 11.554688 63.976562 12.476562 63.976562 13.835938 C 63.976562 14.757812 63.539062 15.539062 62.476562 16.476562 C 60.789062 17.976562 60.398438 18.554688 60.398438 19.742188 L 60.398438 20.835938 Z M 62.195312 22.742188 L 60.398438 22.742188 L 60.398438 24.820312 L 62.195312 24.820312 Z M 10 10.242188 "/>
</g>
</svg>
"""
cairosvg.svg2png(bytestring=svg_code,write_to='output.png')
