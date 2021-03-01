# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
  path "/etc/apt/sources.list"
end
execute 'apt_update' do
  command 'apt-get update'
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
  path "/etc/ntp.conf"
end
execute 'ntp_restart' do
  command 'service ntp restart'
end

package "python3"
package "python3-pip"

#this installs django
execute "pip3 install django" do
  not_if "pipe list | grep django"
end

package "python-django-common"


#packages for geo
package "gdal-bin"
package "libgdal-dev"
package "python3-gdal"
package "binutils"
package "libproj-dev"
package "libsqlite3-mod-spatialite"

execute "pip3_install" do
  command 'pip3 install psycopg2 geoip2'
end

#install django reviews
execute "pip3_install" do
  command 'pip3 install django-rated-reviews'
end


package "postgresql"
package "postgresql-contrib"
package "postgresql-client-common"
package "postgis"
package "postgresql-10"

#package "sqlite3"
#package "spatialite-bin"

execute 'create database' do
  command 'sudo -u postgres psql -c "CREATE DATABASE myproject;" '
end

execute 'create user' do 
  command "sudo -u postgres psql -c \"CREATE USER myprojectuser WITH PASSWORD 'password'; \" " 
end

execute "alter user" do 
  command 'sudo -u postgres psql -c "ALTER ROLE myprojectuser SET client_encoding TO \'utf8\'; "'
  command 'sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;" '
end

execute "create extension" do 
  command 'sudo -u postgres psql myproject postgres -c  "CREATE EXTENSION postgis;"'
end

execute "initial migration" do
  user 'vagrant'
  cwd '/home/vagrant/project/mysite'
  command 'python3 manage.py migrate wee 0002_auto_20200808_0048'

end

#not necessary anymore to alter if migrations are edited
execute 'alter washroom' do 
  command 'sudo -u postgres psql myproject postgres -c "ALTER TABLE wee_washroom ALTER COLUMN name TYPE text;"'
  command 'sudo -u postgres psql myproject postgres -c "ALTER TABLE wee_washroom ALTER COLUMN opening_hours TYPE text;"'
  command 'sudo -u postgres psql myproject postgres -c "ALTER TABLE wee_washroom ALTER COLUMN id TYPE bigint;"'
end

execute 'alter others' do
  command 'sudo -u postgres psql myproject postgres -c "ALTER TABLE wee_review ALTER COLUMN id TYPE bigint;"'
  command 'sudo -u postgres psql myproject postgres -c "ALTER TABLE wee_post ALTER COLUMN id TYPE bigint;"'
  command 'sudo -u postgres psql myproject postgres -c "ALTER TABLE wee_review ALTER COLUMN comment TYPE text;"'
  command 'sudo -u postgres psql myproject postgres -c "ALTER TABLE wee_post ALTER COLUMN title TYPE text;"'
end

execute 'migrate' do
  user 'vagrant'
  cwd '/home/vagrant/project/mysite'
  command 'python3 manage.py migrate'
end


# set up nginx server
package 'nginx'
cookbook_file 'nginx-default' do
  path '/etc/nginx/sites-enabled/default'
end
service 'nginx' do
  action :restart
end
execute 'install-uwsgi' do
  command 'pip3 install uwsgi'
end
execute 'startup' do
  command 'sudo /usr/local/bin/uwsgi --ini /home/vagrant/project/mysite/uwsgi.ini --daemonize /var/log/mysite.log'
end