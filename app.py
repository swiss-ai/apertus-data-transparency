import gradio as gr
import os

def create_app():
    # Custom CSS for better styling
    custom_css = """
    /* Global font size increase */
    .gradio-container, .gradio-container * {
        font-size: 16px !important;
    }
    
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        font-size: 16px;
    }
    .banner-container {
        text-align: center;
        margin-bottom: 30px;
    }
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0 10px 0;
        font-weight: bold;
        font-size: 1.4em !important;
    }
    .subsection-header {
        background: #f8f9fa;
        padding: 10px;
        border-left: 4px solid #667eea;
        margin: 15px 0 10px 0;
        font-weight: bold;
        font-size: 1.1em !important;
    }
    .info-box {
        background: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        font-size: 16px !important;
    }
    .info-box p, .info-box li, .info-box ul {
        font-size: 16px !important;
        line-height: 1.6 !important;
    }
    .highlight {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 10px;
        margin: 5px 0;
        font-size: 16px !important;
    }
    .dataset-link {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
        font-size: 16px !important;
    }
    .dataset-link:hover {
        text-decoration: underline;
    }
    .checkbox-yes {
        color: #28a745;
        font-weight: bold;
        font-size: 16px !important;
    }
    .checkbox-no {
        color: #dc3545;
        font-weight: bold;
        font-size: 16px !important;
    }
    /* Ensure all text elements have larger font */
    h1, h2, h3, h4, h5, h6 {
        font-size: 1.2em !important;
    }
    strong {
        font-size: inherit !important;
    }
    """

    with gr.Blocks(css=custom_css, title="SmolLM3-3B EU Data Transparency") as app:
        
        with gr.Column(elem_classes=["main-container"]):
            # Banner section with images
            with gr.Row():
                with gr.Column(scale=1):
                    try:
                        gr.Image("eu_flag.png", height=180, show_label=False, show_download_button=False, interactive=False, container=False)
                    except:
                        gr.HTML('<div style="height: 120px;"></div>')  # Placeholder if image not found
                
                with gr.Column(scale=1):
                    gr.HTML("""
                    <div style="text-align: center; padding: 20px;">
                        <h1 style="color: #2c3e50; margin: 0; font-size: 3em !important;">SmolLM3-3B</h1>
                        <h2 style="color: #667eea; margin: 10px 0 0 0; font-size: 1.5em !important;">Public Summary of Training Content</h2>
                    </div>
                    """)
                
                with gr.Column(scale=1):
                    try:
                        gr.Image("banner.png", height=180, show_label=False, show_download_button=False, interactive=False, container=False)
                    except:
                        gr.HTML('<div style="height: 120px;"></div>')  # Placeholder if image not found

            gr.HTML("""
                <div style="text-align: center; margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 10px;">
                    <p style="color: #6c757d; margin: 0;">
                        This Space contains the transparency report for the <a href="https://huggingface.co/HuggingFaceTB/SmolLM3-3B">SmolLM3-3B</a> GPAI model developped by <a href="https://huggingface.co/">Hugging Face</a> following the guidelines provided by the AI Office.<br/>
                        For more information, see the <a href="https://digital-strategy.ec.europa.eu/en/library/explanatory-notice-and-template-public-summary-training-content-general-purpose-ai-models" class="dataset-link">Explanatory Notice and Template</a>
                    </p>
                </div>
                <div style="margin: 30px 0; padding: 20px; background: linear-gradient(90deg, #e3f2fd 0%, #f3e5f5 100%); border-radius: 10px; border-left: 5px solid #667eea;">
                    <h3 style="color: #2c3e50; margin-top: 0; font-size: 1.3em !important;"><strong>📋 TL;DR</strong></h3>
                    <p style="font-size: 16px !important; line-height: 1.6; margin: 10px 0;"><strong>SmolLM3-3B</strong> is a state-of-the-art 3-billion parameter language model by <strong>Hugging Face</strong> trained on <strong>10+ trillion tokens</strong> from publicly available datasets including web documents, scientific articles, and code.
                    Training focused on <strong>6 EU languages</strong> plus others. The model uses <strong>only public datasets</strong> (no commercial licensing, user data, or synthetic data).
                    Data processing was done by the original component dataset curators with <strong>varied approaches to TDM and filtering</strong> that typically include compliance with robots.txt and other opt-out mechanisms, and educational content classifiers.</p>
                </div>
            """)

            # Section 1: General Information
            gr.HTML('<div class="section-header">1. General information</div>')
            gr.HTML("""
            <div style="padding: 15px; margin: 10px 0; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #667eea;">
                <p style="margin: 0; font-size: 16px !important; color: #2c3e50;"><strong>TL;DR:</strong> Provider: Hugging Face | Model: SmolLM3-3B | Training: 10+ trillion tokens, 6 EU languages + others</p>
            </div>
            """)
            with gr.Accordion("👇 Click for full information", open=False):
                with gr.Row():
                    with gr.Column():
                        gr.HTML("""
                        <div class="info-box">
                            <div class="subsection-header">1.1. Provider identification</div>
                            <ul>
                                <li><strong>Provider name and contact details:</strong>
                                    <ul>
                                        <li><strong>Hugging Face</strong></li>
                                        <li><strong>Website: <a href="https://huggingface.co" class="dataset-link">https://huggingface.co</a></strong></li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                        """)

                    with gr.Column():
                        gr.HTML("""
                        <div class="info-box">
                            <div class="subsection-header">1.2. Model identification</div>
                            <ul>
                                <li><strong>Versioned model name(s):</strong>
                                    <ul><li><strong>SmolLM3-3B</strong></li></ul>
                                </li>
                                <li><strong>Model dependencies:</strong>
                                    <ul><li><strong>None</strong></li></ul>
                                </li>
                            </ul>
                        </div>
                        """)

                gr.HTML("""
                <div class="info-box">
                    <div class="subsection-header">1.3. Modalities, overall training data size and other characteristics</div>
                    <ul>
                        <li><strong>TEXT</strong>
                            <ul>
                                <li><strong>Size:</strong> <strong>more than 10 trillion tokens</strong></li>
                                <li>The training corpus for SmolLM3 is made up of several publicly accessible large datasets containing web documents, scientific articles, software code, and synthetically generated textbooks and mathematical data for pre-training in addition to several mid-training and fine-tuning datasets to enable chat interactions, instruction-following and task-solving behaviors.</li>
                            </ul>
                        </li>
                        <li><strong>Latest date of data acquisition/collection for model training:</strong>
                            <ul>
                                <li>The training dataset is made up of different subsets with different publication and cutoff dates. For pre-training, the earliest dataset was last updated on 4/3/2024 (Stack v2), and the latest on 2/19/2025 (FineWeb2-HQ)</li>
                            </ul>
                        </li>
                        <li><strong>Description of the linguistic characteristics of the overall training data:</strong>
                            <ul>
                                <li>The overall training process focuses on 6 languages that are all Union languages: English, French, Spanish, German, Italian, and Portuguese. In addition, pre-training intentionally included smaller quantities of data in Mandarin Chinese, Russian, Persian, Japanese, Korean, Vietnamese, Hindi, Thai, and Greek. Other languages may have been included due to the limitations of automatic language identification in filtering stages.</li>
                            </ul>
                        </li>
                        <li><strong>Other relevant characteristics of the overall training data:</strong>
                            <ul>
                                <li>The training data also includes software code in the programming languages included in the Stack v2 dataset (16 languages including C, Python, Java, Markdown, HTML, Shell, etc.).</li>
                            </ul>
                        </li>
                    </ul>
                </div>
                """)

            # Section 2: Data Sources
            gr.HTML('<div class="section-header">2. List of data sources</div>')
            gr.HTML("""
            <div style="padding: 15px; margin: 10px 0; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #667eea;">
                <p style="margin: 0; font-size: 16px !important; color: #2c3e50;"><strong>TL;DR:</strong> ✅ Publicly available datasets (DCLM, FineWeb, Stack v2, etc.) | ❌ No commercial licensing, crawling, user data, or private synthetic data</p>
            </div>
            """)
            with gr.Accordion("👇 Click for full information", open=False):
                gr.HTML("""
                <div class="info-box">
                    <div class="subsection-header">2.1. Publicly available datasets</div>
                    <ul>
                        <li><strong>Have you used publicly available datasets to train the model?</strong>
                            <ul><li><strong><span class="checkbox-yes">☑ Yes</span></strong></li></ul>
                        </li>
                        <li><strong>If yes, specify the modality(ies) of the content covered by the datasets concerned:</strong>
                            <ul><li><strong><span class="checkbox-yes">☑ Text</span></strong></li></ul>
                        </li>
                        <li><strong>List of large publicly available datasets:</strong>
                            <ul>
                                <li>DCLM: <a href="https://hf.co/datasets/mlfoundations/dclm-baseline-1.0" class="dataset-link">https://hf.co/datasets/mlfoundations/dclm-baseline-1.0</a></li>
                                <li>FineWeb-Edu: <a href="https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu" class="dataset-link">https://hf.co/datasets/HuggingFaceFW/fineweb-edu</a></li>
                                <li>FineWeb2: <a href="https://huggingface.co/datasets/epfml/FineWeb2-HQ" class="dataset-link">https://hf.co/datasets/epfml/FineWeb2-HQ</a></li>
                                <li>Stack V2: <a href="https://hf.co/datasets/bigcode/the-stack-v2" class="dataset-link">https://hf.co/datasets/bigcode/the-stack-v2</a></li>
                                <li>pes2o: <a href="https://hf.co/datasets/allenai/peS2o" class="dataset-link">https://hf.co/datasets/allenai/peS2o</a></li>
                                <li>SmolTalk2: <a href="https://huggingface.co/datasets/HuggingFaceTB/smoltalk2" class="dataset-link">https://hf.co/datasets/HuggingFaceTB/smoltalk2</a></li>
                            </ul>
                        </li>
                        <li><strong>General description of other publicly available datasets not listed above:</strong>
                            <ul>
                                <li>In addition to the large datasets cited above, many additional publicly available datasets were added to target specific domains, including several math datasets made up of both web-filtered and synthetic data, Wikipedia data, "reasoning data" generated by selected large models on diverse problems, Jupyter notebooks for code, and synthetically generated textbooks; all in English language or software code. The full list of pre-training datasets is available at the following URL: <a href="https://hf.co/collections/HuggingFaceTB/smollm3-pretraining-datasets-685a7353fdc01aecde51b1d9" class="dataset-link">https://hf.co/collections/HuggingFaceTB/smollm3-pretraining-datasets-685a7353fdc01aecde51b1d9</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
                """)

                gr.HTML("""
                <div class="info-box">
                    <div class="subsection-header">2.2. Private non-publicly available datasets obtained from third parties</div>
                    
                    <h4>2.2.1. Datasets commercially licensed by rightsholders or their representatives</h4>
                    <ul>
                        <li><strong>Have you concluded transactional commercial licensing agreement(s) with rightsholder(s) or with their representatives?</strong>
                            <ul><li><strong><span class="checkbox-no">☐ No</span></strong></li></ul>
                        </li>
                    </ul>
                    
                    <h4>2.2.2. Private datasets obtained from other third parties</h4>
                    <ul>
                        <li><strong>Have you obtained private datasets from third parties that are not licensed as described in Section 2.2.1, such as data obtained from providers of private databases, or data intermediaries?</strong>
                            <ul><li><strong><span class="checkbox-no">☐ No</span></strong></li></ul>
                        </li>
                    </ul>
                </div>
                """)

                with gr.Row():
                    with gr.Column():
                        gr.HTML("""
                        <div class="info-box">
                            <div class="subsection-header">2.3. Data crawled and scraped from online sources</div>
                            <ul>
                                <li><strong>Were crawlers used by the provider or on behalf of?</strong>
                                    <ul><li><strong><span class="checkbox-no">☐ No</span></strong></li></ul>
                                </li>
                            </ul>
                        </div>
                        """)
                    
                    with gr.Column():
                        gr.HTML("""
                        <div class="info-box">
                            <div class="subsection-header">2.4. User data</div>
                            <ul>
                                <li><strong>Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?</strong>
                                    <ul><li><strong><span class="checkbox-no">☐ No</span></strong></li></ul>
                                </li>
                                <li><strong>Was data collected from user interactions with the provider's other services or products used to train the model?</strong>
                                    <ul><li><strong><span class="checkbox-no">☐ No</span></strong></li></ul>
                                </li>
                            </ul>
                        </div>
                        """)

                with gr.Row():
                    with gr.Column():
                        gr.HTML("""
                        <div class="info-box">
                            <div class="subsection-header">2.5. Synthetic data</div>
                            <ul>
                                <li><strong>Was synthetic AI-generated data created by the provider or on their behalf to train the model?</strong>
                                    <ul><li><strong><span class="checkbox-no">☐ No</span></strong></li></ul>
                                </li>
                            </ul>
                        </div>
                        """)
                    
                    with gr.Column():
                        gr.HTML("""
                        <div class="info-box">
                            <div class="subsection-header">2.6. Other sources of data</div>
                            <ul>
                                <li><strong>Have data sources other than those described in Sections 2.1 to 2.5 been used to train the model?</strong>
                                    <ul><li><strong><span class="checkbox-no">☐ No</span></strong></li></ul>
                                </li>
                            </ul>
                        </div>
                        """)

            # Section 3: Data Processing
            gr.HTML('<div class="section-header">3. Data processing aspects</div>')
            gr.HTML("""
            <div style="padding: 15px; margin: 10px 0; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #667eea;">
                <p style="margin: 0; font-size: 16px !important; color: #2c3e50;"><strong>TL;DR:</strong> TDM rights: robots.txt baseline otherwise dataset-dependent | Content filtering: Dataset-dependent including educational classifiers</p>
            </div>
            """)
            with gr.Accordion("👇 Click for full information", open=False):
                gr.HTML("""
                <div class="info-box">
                    <div class="subsection-header">3.1. Respect of reservation of rights from text and data mining exception or limitation</div>
                    <ul>
                        <li><strong>Describe the measures implemented before model training to respect reservations of rights from the TDM exception or limitation before and during data collection, including the opt-out protocols and solutions honoured by the provider or, as applicable, by third parties from which datasets have been obtained:</strong>
                            <ul>
                                <li>The training corpus for SmolLM3-3B is made up of diverse pre-existing public datasets maintained by various organizations who still have their own approach to managing the TDM exception. All crawl-based data in the datasets uses the CommonCrawl archives which comply with robots.txt. Some datasets such as the Stack v2 additionally offer general opt-out mechanisms. For each dataset, the latest publicly available version was used to ensure propagation of any rights reservation expressed to the dataset custodian.</li>
                            </ul>
                        </li>
                    </ul>
                </div>
                """)

                gr.HTML("""
                <div class="info-box">
                    <div class="subsection-header">3.2. Removal of illegal content</div>
                    <ul>
                        <li><strong>General description of measures taken:</strong>
                            <ul>
                                <li>Each of the component datasets leveraged is the product of a distinct curation effort by its custodians to select the most desirable content. The specific approaches can typically be found in the dataset documentation. Among other factors, most of the datasets take the approach of using classifiers to identify "highly educational" samples that lowers the likelihood of illegal content.</li>
                            </ul>
                        </li>
                    </ul>
                </div>
                """)


    return app

# Create the demo instance directly for Gradio auto-reload
demo = create_app()

if __name__ == "__main__":
    demo.launch(share=True, show_error=True) 