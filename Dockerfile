#Dockerfile for Google Custom Search
FROM continuumio/anaconda3

RUN conda update -n base -c defaults conda &&\
	conda install -c conda-forge textblob

RUN pip install --upgrade pip &&\
	conda install -c conda-forge spacy &&\
	pip install networkx datasketch graphviz statistics pytextrank pdfminer.six

RUN apt-get update &&\
    apt-get install -y vim

RUN python -m spacy download en

#ADD jupyter_notebook_config.json /opt/conda/etc/jupyter/
#	touch /root/.jupyter/jupyter_notebook_config.py &&\
#	echo "c.NotebookApp.ip = ‘localhost’" >> /root/.jupyter/jupyter_notebook_config.py
#RUN   sed -i "some_old_line|some_old_line_to_be_replaced|replacement_line |some_old_line" /root/.jupyter/jupyter_notebook_config.py
WORKDIR /opt/Programs

CMD ["bash"]