#! /bin/bash

echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >> /etc/apt/sources.list.d/ondrej-php-trusty.list && \
	echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >> /etc/apt/sources.list.d/newrelic.list && \
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 4F4EA0AAE5267A6C && \
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B31B29E5548C16BF

apt-get update && \
	apt-get -y install \
		apache2 \
		libapache2-mod-php7.0 \
		php7.0-cli \
		php7.0-curl \
		php7.0-gd \
		php7.0-mbstring \
		php7.0-xml \
		newrelic-php5 \
		vim-tiny && \
	apt-get autoremove -y && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

