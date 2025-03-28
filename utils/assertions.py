def assert_feedback(feedback_component, should_pass):
    if should_pass:
        assert feedback_component.is_visible() == False
    else:
        assert feedback_component.is_visible() == True

def assert_confirmation_page(confirmation_page_object, should_pass):
    if should_pass:
        assert confirmation_page_object.is_displayed() == True
    else:
        assert confirmation_page_object.is_displayed() == False
