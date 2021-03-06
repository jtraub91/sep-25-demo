def present(
    name,
    uid=None,
    gid=None,
    usergroup=None,
    groups=None,
    optional_groups=None,
    remove_groups=True,
    home=None,
    createhome=True,
    password=None,
    hash_password=False,
    enforce_password=True,
    empty_password=False,
    shell=None,
    unique=True,
    system=False,
    fullname=None,
    roomnumber=None,
    workphone=None,
    homephone=None,
    other=None,
    loginclass=None,
    date=None,
    mindays=None,
    maxdays=None,
    inactdays=None,
    warndays=None,
    expire=None,
    win_homedrive=None,
    win_profile=None,
    win_logonscript=None,
    win_description=None,
    nologinit=False,
    allow_uid_change=False,
    allow_gid_change=False,
    register=None
):
    ret = __states__["user.present"](
        name,
        uid=uid,
        gid=gid,
        usergroup=usergroup,
        groups=groups,
        optional_groups=optional_groups,
        remove_groups=remove_groups,
        home=home,
        createhome=createhome,
        password=password,
        hash_password=hash_password,
        enforce_password=enforce_password,
        empty_password=empty_password,
        shell=shell,
        unique=unique,
        system=system,
        fullname=fullname,
        roomnumber=roomnumber,
        workphone=workphone,
        homephone=homephone,
        other=other,
        loginclass=loginclass,
        date=date,
        mindays=mindays,
        maxdays=maxdays,
        inactdays=inactdays,
        warndays=warndays,
        expire=expire,
        win_homedrive=win_homedrive,
        win_profile=win_profile,
        win_logonscript=win_logonscript,
        win_description=win_description,
        nologinit=nologinit,
        allow_uid_change=allow_uid_change,
        allow_gid_change=allow_gid_change,
    )
    __context__[register] = ret["changes"].get("uid")
    return ret
