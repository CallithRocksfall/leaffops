set -gx EDITOR nvim
function y
    set tmp (mktemp -t "yazi-cwd.XXXXXX")
    yazi $argv --cwd-file="$tmp"
    if read -z cwd <"$tmp"; and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
        builtin cd -- "$cwd"
    end
    rm -f -- "$tmp"
end
if status is-interactive
    # Commands to run in interactive sessions can go here
end
oh-my-posh init fish --config ~/.config/OhMyPosh/leaf.omp.json | source
