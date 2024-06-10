import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate


# df = pd.read_csv("./mobile_dataset.csv")
# target = "price_range"


def generate_prompt(data_sample):
    prompt = """
    Given the following Tabular Data:

    {data_sample}

    Provide detailed analysis and insights on {target_variable} based on other features, data trends, anomalies, and significant findings in bullet points.
    """

    return PromptTemplate(input_variables=['data_sample', 'target_variable'], template=prompt)


def generate_data_samples(df, num_samples=30):
    if num_samples == "all":
        num_samples = len(df)
    else:
        num_samples = int(num_samples)

    data_sample = df.sample(num_samples).to_string(index=False)
    return data_sample

def generate_response(df, target):
    data_samples = generate_data_samples(df)
    prompt = generate_prompt(data_samples)
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    out_parser = StrOutputParser()
    chain = prompt|llm|out_parser
    response = chain.invoke({"data_sample":data_samples, "target_variable":target})
    return response
