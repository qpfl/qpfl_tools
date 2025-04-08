from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_championship_banner(year: str, team_name: str, ordinal: str, league_name: str = "QPFL", laurel_path: str = "assets/laurel.png", output_filename: str = "qpfl_banners", mini: bool = False):
    """
    Generate a QPFL Champion banner with customizable year, team name, and ordinal.
    
    Args:
        year (str): The year to display on the banner
        team_name (str): The team name to display on the banner
        ordinal (str): The ordinal number (e.g., "5TH", "6TH") for the annual event
        league_name (str): The name of the league (default is "QPFL")
        laurel_path (str): Path to the laurel wreath image
        output_filepath (str): Filename for the output image
    """
    # define colors and dimensions
    if league_name == "OPFL":
        background_cream_color = (255, 248, 240)
        border_blue_color = (0, 35, 102)
        text_blue_color = (0, 35, 102)
    else:
        background_cream_color = (240, 248, 255)
        border_blue_color = (0, 35, 102)
        text_blue_color = (0, 35, 102)
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
    ], outline=border_blue_color, width=border_width)
    
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
    
    draw.text((width//2, 120), f"{ordinal} ANNUAL", fill=text_blue_color, font=title_font, anchor="mm")
    draw.text((width//2, 250), league_name, fill=text_blue_color, font=champion_font, anchor="mm")
    
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
    draw.polygon(shield_points, fill=text_blue_color)
    draw.text((width//2, shield_top + shield_height//2 - 10), league_name, fill=background_cream_color, font=qpfl_shield_font, anchor="mm")
    
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
    
    draw.text((width//2, 620), "CHAMPION", fill=text_blue_color, font=champion_font, anchor="mm")
    
    lines = textwrap.wrap(team_name.upper(), width=15)
    y_text = 750
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=team_name_font)
        text_height = bottom - top
        
        draw.text((width//2, y_text), line, fill=text_blue_color, font=team_name_font, anchor="mm")
        y_text += text_height + 10
    
    draw.text((width//2, 1000), str(year), fill=text_blue_color, font=year_font, anchor="mm")
    image = image.resize((105, 150), Image.Resampling.LANCZOS)
    output_filename = f"{output_filename}_{year}.png"
    image.save(output_filename) 
    print(f"Banner saved as {output_filename}")
    return image

def generate_opfl_banners():
    output_filename = "opfl_banners/opfl_champion"
    # Keep the laurel image in the same directory as this script
    laurel_path = "assets/laurel.png"
    champions = [
        (1988, "Bill"),
        (1989, "Chris"),
        (1990, "Bill"),
        (1991, "Steve M."),
        (1992, "Steve L."),
        (1993, "Bill"),
        (1994, "Bill"),
        (1995, "Chris"),
        (1996, "Steve/J"),
        (1997, "Kemp"),
        (1998, "Eric S."),
        (1999, "Eric S."),
        (2000, "John"),
        (2001, "Kemp/Rams"),
        (2002, "Adam/Nick"),
        (2003, "Kirk"),
        (2004, "Kreg"),
        (2005, "Jarrett"),
        (2006, "Kirk"),
        (2007, "Eric S."),
        (2008, "Steve L."),
        (2009, "Steve L."),
        (2010, "Kirk/David"),
        (2011, "Bill/Jill"),
        (2012, "Kevin"),
        (2013, "Jarrett"),
        (2014, "Steve L."),
        (2015, "Steve L."),
        (2016, "Kemp/Ad/Miles"),
        (2017, "Kirk/David"),
        (2018, "Adam"),
        (2019, "Andrew"),
        (2020, "Kemp/Ad/Miles"),
        (2021, "Kemp/Ad/Miles"),
        (2022, "Jarrett/Matt & Wes"),
        (2023, "Kemp/Ad/Miles"),
        (2024, "Kemp/Ad/Miles")
    ]

    # Function to convert number to ordinal
    def get_ordinal(n):
        if 10 <= n % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
        return f"{n}{suffix}"

    # Loop through each champion and create a banner
    for index, (year, team_name) in enumerate(champions, 1):
        ordinal = get_ordinal(index)
        
        create_championship_banner(
            year=year, 
            team_name=team_name, 
            ordinal=ordinal,
            laurel_path=laurel_path,
            league_name="OPFL",
            output_filename=output_filename,
            mini=True)

def regenerate_all_qpfl_banners(mini: bool = False):
    """
    Regenerate all banners for the QPFL.
    """
    years = ["2020", "2021", "2022", "2023", "2024"]
    ordinals = ["1ST", "2ND", "3RD", "4TH", "5TH"]
    team_names = ["Sandusky's Secret", "Alvin, Dalvin, and the Chipmunks", "Mahomes' Beermeister", "Music City Jahmyricle", "All Roads Lead to Rome"]

    for year, ordinal, team_name in zip(years, ordinals, team_names):
        create_championship_banner(year=year, team_name=team_name, ordinal=ordinal, mini=mini)

if __name__ == "__main__":
    generate_opfl_banners()
