%define		plugin	check_bacula_log
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check bacula status via bacula log
Name:		nagios-plugin-%{plugin}
Version:	0.3
Release:	3
License:	GPL v2
Group:		Networking
Source0:	%{plugin}.pl
Source1:	%{plugin}.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Backup-and-Recovery/Bacula/nagios%252Dcheck_bacula/details
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
Requires:	nagios-plugins-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%define		_noautoreq	'perl(utils)'

%description
Nagios plugin that checks whether the backups made for today with the
Bacula backup system were succesful.

This requires the Nagios user to have read access to the bacula log
file.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}