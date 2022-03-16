FROM centos:7

ENV container docker

COPY keepalive.sh /usr/bin/
COPY activationcode.txt /usr/bin/
COPY yum.repo /etc/yum.repos.d/Tenable.repo
COPY gpg.key /etc/pki/rpm-gpg/RPM-GPG-KEY-Tenable

RUN    yum -y update                                                    \
    && yum -y install nnm yum-utils unzip zip file htop java-11-openjdk make iftop net-tools epel-release                                             \
    && yum -y clean all                                                 \
    && chmod 755 /usr/bin/keepalive.sh                                  \
    && chmod 755 /usr/bin/activationcode.txt                                    \
    && echo -e "export PATH=$PATH:/opt/nnm/bin" >> /etc/bashrc          \
    && echo -e "nnm.local" > /etc/hostname


EXPOSE 8835
CMD "/usr/bin/keepalive.sh"
