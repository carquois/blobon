/home/web/punn.it/bin/python /home/web/punn.it/punn_it/manage.py migrate punns
/home/web/punn.it/bin/python /home/web/punn.it/punn_it/manage.py migrate accounts 
/home/web/punn.it/bin/python /home/web/punn.it/punn_it/manage.py collectstatic --noinput
supervisorctl restart punn_it
