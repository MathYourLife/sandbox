#/bin/bash

sudo apt-get update
sudo apt-get install -y build-essential wget libyaml-dev zlib1g-dev libreadline-dev libssl-dev tk-dev libgdbm-dev openjdk-6-jdk gem

STATUS=0
# wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p374.tar.gz || STATUS=1
# tar xvzf ruby-1.9.3-p374.tar.gz || STATUS=1
cd ruby-1.9.3-p374 || STATUS=1
./configure --prefix=/usr/local/ --enable-shared --disable-install-doc|| STATUS=1
sudo make|| STATUS=1
sudo make install|| STATUS=1

wget http://aphyr.com/riemann/riemann-0.2.4.tar.bz2
tar xvfj riemann-0.2.4.tar.bz2
cd riemann-0.2.4

sudo gem install riemann-client riemann-tools riemann-dash