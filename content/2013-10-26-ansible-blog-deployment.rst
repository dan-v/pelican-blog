Ansible Blog Deployment
########################

:date: 2013-10-26 12:00
:tags: ansible,deployment
:category: Project
:author: Dan

Finally got a chance to play around with Ansible_. Ansible is a very lightweight configuration management system based on Python and SSH. 

.. _Ansible: http://www.ansibleworks.com/

I created a very simple project to deploy this blog using Ansible which you can find on Github_. 

.. _Github: https://github.com/dan-v/pelican-blog-ansible/

A quick overview of key components:

* hosts - This is a list of the hosts that you want to configure.
* site.yml - Here two roles and selected (common and blog). This defines what you actually want Ansible to run against the hosts.
* roles/common/tasks - These are some common tasks that you might always want to configure for every deployment. A good example would be firewall configuration.
* roles/blog/tasks - These are all tasks required to deploy this specific blog.
* roles/\*/var - Variables that can be used throughout tasks and templates.
* roles/\*/templates - Template files to be layed down on filesystem with variable substitution.

Once you have Ansible installed, you can just run: ansible-playbook -i hosts site.yml
