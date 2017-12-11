#include <clara.hpp>

using namespace clara;

int main() {
    std::string name;
    auto p = Opt(name, "name")
        ["-n"]["--name"]
        ("the name to use");

    p.parse( Args{ "TestApp", "-n", "Vader" } );
    p.parse( Args{ "TestApp", "--name", "Vader" } );
    p.parse( Args{ "TestApp", "-n:Vader" } );
    p.parse( Args{ "TestApp", "-n=Vader" } );
    p.parse( Args{ "TestApp" } );
    p.parse( Args{ "TestApp", "-f" } );
}