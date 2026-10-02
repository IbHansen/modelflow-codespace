# ModelFlow in GitHub Codespaces

Run **ModelFlow directly in your web browser**, without installing Python, Conda, or ModelFlow on your own computer.

GitHub Codespaces provides a cloud-based Linux environment with Python, ModelFlow, Jupyter, and the necessary dependencies already installed. You can create, run, and modify ModelFlow models in interactive Jupyter notebooks, using the same Python framework as on a local computer.

Each user gets their own Codespace, with a separate working environment and files.

## 1. Launch ModelFlow

**[🚀 Launch ModelFlow in GitHub Codespaces](https://codespaces.new/IbHansen/modelflow-codespace?quickstart=1)**

You need a GitHub account to use Codespaces. If you do not have one, you can [create a free GitHub account](https://github.com/signup).

To get started:

1. Click the **Launch ModelFlow** link above.
2. Sign in to GitHub if necessary.
3. Select **Create codespace** if prompted.
4. GitHub creates your cloud environment and opens VS Code in your browser.

The first launch takes longer because the environment must be built and its Python packages installed. Subsequent launches of the same Codespace are normally faster.

You can also create a Codespace directly from this repository by selecting **Code → Codespaces → Create codespace on main**.

## 2. Open Jupyter Notebook

Once your Codespace has started, the environment automatically launches a Jupyter Notebook server.

A new browser tab should open with the introductory notebook:

`notebooks/start.ipynb`

If the notebook does not open automatically, select the **Ports** tab in VS Code and open the forwarded address for port **8888**.

The introductory notebook is currently a proof of concept and a placeholder. It demonstrates that ModelFlow can be imported and a simple model can be constructed in the Codespace environment. More comprehensive modeling examples can be added later.

To execute a notebook cell, press **Shift+Enter**. To execute the complete notebook, select **Run → Run All Cells**.

You can create additional notebooks, open existing notebooks, or upload your own models and data files.

## 3. Running your own ModelFlow models

The Codespace contains a Python environment named `modelflow`, with ModelFlow installed from the `ibh` Conda channel.

You can use ModelFlow as you would on your own computer, including:

* Creating and solving models using the ModelFlow equation language.
* Loading existing models and their associated data.
* Running baseline simulations, alternative scenarios, and policy experiments.
* Analyzing simulation results and displaying graphs.
* Developing and running Python notebooks using ModelFlow and its dependencies.

In Jupyter notebooks, select the Python kernel associated with the `modelflow` environment.

The Codespace also provides a terminal where you can execute Python scripts, install additional packages, and work with your model files.

## 4. Using JupyterLab or VS Code

You can work with ModelFlow in several ways.

**Jupyter Notebook:** The default interface, which starts automatically when you connect to the Codespace.

**JupyterLab:** A more comprehensive notebook environment with a file browser, multiple notebooks, terminals, and other development tools. You can launch JupyterLab from a Codespace terminal using:

```bash
jupyter lab --no-browser
```

**VS Code:** The browser-based development environment provided by Codespaces. It supports editing Python files, running Jupyter notebooks, using a terminal, and working with Git and GitHub.

All three interfaces use the same underlying Codespace environment.

## 5. Saving your work

Your notebooks and other files are stored in your Codespace and remain available when you stop and later restart that Codespace.

To preserve your work independently of the Codespace, commit and push your changes to a GitHub repository or download your files to your own computer.

**Important:** A Codespace is not intended as permanent file storage. Deleting a Codespace can permanently remove files that have not been saved elsewhere.

## 6. Stopping and restarting

When you finish working, stop your Codespace to avoid unnecessary consumption of your GitHub Codespaces allowance.

You can manage your Codespaces at:

https://github.com/codespaces

From this page, you can stop, restart, open, or delete an existing Codespace.

GitHub Codespaces has usage allowances and billing conditions. Check your GitHub account's Codespaces settings for the limits applicable to your account.

## 7. Security

The Jupyter server is configured to run without a separate Jupyter authentication token. Access is therefore protected by GitHub Codespaces' private port forwarding.

**Keep port 8888 private. Do not change its visibility to public.**

Making the port public could allow other people to access your Jupyter environment and execute code.

## 8. Further information

For more information about ModelFlow and its use with macroeconomic models, see:

**[Running MFMod and Other Models in Python with ModelFlow](https://worldbank.github.io/MFMod-ModelFlow/content/introduction.html)**

For general information about GitHub Codespaces, see the [GitHub Codespaces documentation](https://docs.github.com/en/codespaces).
