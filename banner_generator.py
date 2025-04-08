from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_qpfl_banner(year: str, team_name: str, ordinal: str  = "5TH", laurel_path: str = "laurel.png", output_filename: str = "qpfl_banner.png"):
    """
    Generate a QPFL Champion banner with customizable year, team name, and ordinal.
    
    Args:
        year (str): The year to display on the banner
        team_name (str): The team name to display on the banner
        ordinal (str): The ordinal number (e.g., "5TH", "6TH") for the annual event
        laurel_path (str): Path to the laurel wreath image
        output_filename (str): Filename for the output image
    """
    # define colors and dimensions
    background_cream_color = (248, 240, 227)
    border_red_color = (128, 32, 32)
    text_red_color = (128, 32, 32)
    width = 800
    height = 1200
    border_width = 20
    
    image = Image.new('RGB', (width, height), background_cream_color)
    draw = ImageDraw.Draw(image)
    

    draw.polygon([
        (border_width, border_width),
        (width - border_width, border_width),
        (width - border_width, height - 250),
        (width // 2, height - border_width),
        (border_width, height - 250),
    ], outline=border_red_color, width=border_width)
    
    try:
        title_font = ImageFont.truetype("Times New Roman Bold.ttf", 100)
        champion_font = ImageFont.truetype("Times New Roman Bold.ttf", 120)
        team_name_font = ImageFont.truetype("Times New Roman Bold.ttf", 80)
        year_font = ImageFont.truetype("Times New Roman Bold.ttf", 120)
        qpfl_shield_font = ImageFont.truetype("Times New Roman Bold.ttf", 30)
    except IOError:
        title_font = ImageFont.load_default()
        champion_font = ImageFont.load_default()
        team_name_font = ImageFont.load_default()
        year_font = ImageFont.load_default()
        qpfl_shield_font = ImageFont.load_default()
    
    draw.text((width//2, 120), f"{ordinal} ANNUAL", fill=text_red_color, font=title_font, anchor="mm")
    draw.text((width//2, 250), "QPFL", fill=text_red_color, font=champion_font, anchor="mm")
    
    shield_width = 200
    shield_height = 220
    shield_top = 350
    
    shield_points = [
        (width//2 - shield_width//2, shield_top),
        (width//2 + shield_width//2, shield_top),
        (width//2 + shield_width//2, shield_top + shield_height - 40),
        (width//2, shield_top + shield_height),
        (width//2 - shield_width//2, shield_top + shield_height - 40),
    ]
    draw.polygon(shield_points, fill=text_red_color)
    draw.text((width//2, shield_top + shield_height//2 - 10), "QPFL", fill=background_cream_color, font=qpfl_shield_font, anchor="mm")
    
    try:
        laurel_img = Image.open(laurel_path)
        
        if laurel_img:
            if laurel_img.mode != 'RGBA':
                laurel_img = laurel_img.convert('RGBA')
            
            laurel_size = 180
            laurel_img = laurel_img.resize((laurel_size, laurel_size))
            laurel_processed = Image.new('RGBA', laurel_img.size, (0, 0, 0, 0))
            for x in range(laurel_img.width):
                for y in range(laurel_img.height):
                    r, g, b, a = laurel_img.getpixel((x, y))
                    if r < 50 and g < 50 and b < 50 and a > 100:
                        laurel_processed.putpixel((x, y), background_cream_color + (255,))
            
            laurel_position = (
                width//2 - laurel_size//2,
                shield_top + shield_height//2 - laurel_size//2
            )
            image.paste(laurel_processed, laurel_position, laurel_processed)
            
    except Exception as e:
        print(f"Error loading laurel image: {e}")
    
    draw.text((width//2, 620), "CHAMPION", fill=text_red_color, font=champion_font, anchor="mm")
    
    lines = textwrap.wrap(team_name.upper(), width=15)
    y_text = 750
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=team_name_font)
        text_height = bottom - top
        
        draw.text((width//2, y_text), line, fill=text_red_color, font=team_name_font, anchor="mm")
        y_text += text_height + 10
    
    draw.text((width//2, 1000), str(year), fill=text_red_color, font=year_font, anchor="mm")
    
    image = image.resize((105, 150), Image.Resampling.LANCZOS)
    output_filename = f"qpfl_banners/{output_filename}_{year}.png"
    image.save(output_filename) 
    print(f"Banner saved as {output_filename}")
    return image


if __name__ == "__main__":

    # Modify these variables to customize the banner
    year = "2020"
    ordinal = "1st"
    team_name = "Sandusky's Secret"

    output_filename = "qpfl_banner"
    # Keep the laurel image in the same directory as this script
    laurel_path = "assets/laurel.png"
    team_name = team_name.upper()
    create_qpfl_banner(
        year=year, 
        team_name=team_name, 
        ordinal=ordinal,
        laurel_path=laurel_path,
        output_filename=output_filename
    )
