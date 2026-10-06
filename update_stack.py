import os
import base64

WORKSPACE = "/Users/Apple/Desktop/github"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")
IMAGE_PATH = os.path.join(WORKSPACE, "image.png")

def generate_stack_svg():
    with open(IMAGE_PATH, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1672 941" width="100%" height="auto" fill="none">
  <defs>
    <linearGradient id="stack-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#1e293b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>
    <clipPath id="stack-rounded">
      <rect width="1672" height="941" rx="20" ry="20" />
    </clipPath>
  </defs>
  <g clip-path="url(#stack-rounded)">
    <image href="data:image/png;base64,{b64}" width="1672" height="941" />
    <rect x="1" y="1" width="1670" height="939" rx="19" fill="none" stroke="url(#stack-border-grad)" stroke-width="2" />
  </g>
</svg>'''

if __name__ == "__main__":
    svg_content = generate_stack_svg()
    target_path = os.path.join(ASSETS_DIR, "stack.svg")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Successfully generated and updated: {target_path}")
