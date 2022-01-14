mongo -- "$MONGO_DB" <<EOF
    var rootUser = '$MONGO_ROOT_USER';
    var rootPassword = '$MONGO_ROOT_PASSWD';
    var admin = db.getSiblingDB('admin');
    admin.auth(rootUser, rootPassword);

    var user = '$MONGO_USER';
    var passwd = '$MONGO_USER_PASSWD';
    db.createUser({user: user, pwd: passwd, roles: ["readWrite"]});
EOF
