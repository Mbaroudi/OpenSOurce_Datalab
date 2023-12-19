from dagster import pipeline, solid
import dagstermill

@solid
def example_solid(context):
    notebook_path = "/path/in/container/for/notebooks/my_notebook.ipynb"  # Adjust this path
    dagstermill.execute_notebook(
        notebook_path=notebook_path,
        output_notebook_path="/tmp/output.ipynb",
        context=context
    )

@pipeline
def my_pipeline():
    example_solid()
