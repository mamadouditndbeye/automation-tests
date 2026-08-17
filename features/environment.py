from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get("https://duckduckgo.com")

def after_step(context, step):
    if step.status == "failed":
        context.driver.save_screenshot(f"echec_{step.name}.png")

def after_scenario(context, scenario):
    context.driver.quit()