from features.steps.step_imp import StepImp
from pages.Base import Base

def before_scenario(context, scenario):
    # Attach the StepImp instance to the context object
    context.step_impl = StepImp()



def after_scenario(context, scenario):
    # Clean up if necessary
    context.step_impl = None