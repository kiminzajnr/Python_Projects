# Still the initial script I used as a standalone
# Some sections aren't used in the advanced implementation, ignore
username="ubuntu"
public_key="$1"
shift

status="Authorized keys updated successfully on"
ssh_options="-o StrictHostKeyChecking=no"

for server in "$@"; do
    echo "Updating authorized_keys on $server"
    # priv.key is the private key pinned in the mentor channel
    ssh $ssh_options -i priv.key "$username@$server" "echo '$public_key' >> ~/.ssh/authorized_keys"
    if [ $? -eq 0 ]; then
        echo "$status $server"
    else
        echo "Error occurred while updating authorized_keys on $server"
    fi
done
