from behave import *
from step_imp import StepImp


step_impl = StepImp()

@given(u'Launch Home screen')
def launch_home_screen(context):
    context.step_impl.launch_page()


@then(u'Verify Scrolling Ad')
def verify_scrolling_ad(context):
    context.step_impl.verify_slider_row()



@then(u'verify category Text')
def verify_category_text(context):
    context.step_impl.verify_category_text()


@then(u'Verify Brand Text')
def verify_brand_text(context):
    context.step_impl.verify_brand_text()


@then(u'verify feature Text')
def verify_feature_text(context):
    context.step_impl.verify_features_item_text()



@then(u'Scroll down to bottom of page')
def scroll_down_to_bottom_of_page(context):
    context.step_impl.scroll_to_bottom()


@then(u'Verify Subscription Text')
def verify_subscription_text(context):
    context.step_impl.verify_subscription_text()

@then(u'click view product')
def click_view_product(context):
    context.step_impl.select_item()


@then(u'Verify Product URL open')
def verify_product_url_open(context):
    context.step_impl.product_title()


@then(u'Verify Product title')
def verify_product_title(context):
    context.step_impl.current_url()



@then(u'click signup up')
def click_signup_up(context):
    context.step_impl.click_sigup_up()



@then(u'enter name and mail in new user section')
def enter_name_and_mail_in_new_user_section(context):
    context.step_impl.enter_new_user_name_and_email()


@when(u'Validate Enter account Information text')
def validate_enter_account_information_text(context):
    context.step_impl.validate_enter_deatils_text()


@then(u'Enter mandatory feilds')
def enter_mandatory_feilds(context):
    context.step_impl.enter_star_feilds()


@then(u'click Create Account')
def click_create_account(context):
    context.step_impl.click_create_acc()



@then(u'Verify Account Created MSG')
def verify_account_created_msg(context):
    context.step_impl.verify_acc_create_cmp_msg()


@then(u'Enter existed "{username}" and "{password}"')
def enter_existed_username_and_password(context, username, password):
    context.step_impl.enter_existed_user_details(username, password)


@then(u'click login')
def click_login(context):
    context.step_impl.click_login()

@then(u'Verify Logout button in screen')
def verify_logout_button_in_screen(context):
    context.step_impl.logout_button()


@when(u'click on products')
def click_on_products(context):
    context.step_impl.click_on_product()


@when(u'Search for {product}')
def search_for_product(context, product):
    context.step_impl.search_for_product(product)


@when(u'Click Search icon')
def click_search_icon(context):
    context.step_impl.click_on_search_icon()


@then(u'Validate results')
def validate_results(context):
    context.step_impl.validate_results()


@then(u'close browser')
def close_browser(context):
    context.step_impl.close_brwoser()



