#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <regex>
#include "ghc-filesystem.hpp"

namespace fs = ghc::filesystem;
using namespace std;
ofstream fs;

namespace dgu {

class GoUtil {
	
public:
	map<string,string> considerTable(string filename);
    map<int,int> obsoleteStats(string filename);
};

map<int,int> GoUtil::obsoleteStats(string filename)
{
    ifstream infile;
	infile.open(filename);
	string line;
    regex rx("^id: ");
    regex consid("^consider: ");
    regex obsolete("^is_obsolete: ");

    bool flag = false;
    bool obsflag = false;

    int cons = 0;
    int total = 0;
    map<int, int> count;

    while(getline(infile, line))
    {
        if (regex_search(line,rx))
        {
            flag = true;
        }
        if (flag && regex_search(line, obsolete))
        {
            total++;
            obsflag = true;
            flag = false;
        }
        if (obsflag && regex_search(line, consid))
        {
            cons++;
            obsflag = false;
        }
    }
    count.insert(pair<int,int>(cons,total-cons));

    return(count);
}

map<string,string> GoUtil::considerTable(string filename) 
{
	ifstream infile;
	infile.open(filename);
	string line;
	regex rx("^id: ");
    regex consid("^consider: ");
    regex obsolete("^is_obsolete: ");

	bool flag = false;
    // bool consflag = false;

    string id;
    string considered_id;
    map<string,string> table;

    int counter = 0;

	while (getline(infile,line)) 
	{
		if (regex_search(line,rx)) 
		{
            id = line.substr(4, 10);
		}
        else if (regex_search(line, obsolete)) 
        {
            flag = true;
            continue;
        }
        if (flag)
        {
            if (regex_search(line,consid))
            {
                considered_id = line.substr(10, 10);
			    table.insert(pair<string, string>(id, considered_id));
            }
            else
            {
			    table.insert(pair<string, string>(id, "NA"));
                flag = false;
            }
        }
        counter++;
        if (counter == 1000) break;
	}
	return(table);
}

}

void usage (char * appname) 
{
	cout << appname << " goobofile CMD\n";
	cout << "CMD is considerTable or obsoleteStats. molecular_function argument is optional.\n";
}

int main(int argc, char **argv) 
{

	auto goutil = dgu::GoUtil();

	if (argc < 3) 
		usage(argv[0]);
    else 
	{
        if (!fs::exists(argv[1])) 
		{
			cout << "Error: File " << argv[1] << " does not exists!\n";
			return(0);
		}

        string cmd = string(argv[2]);
        string option = string(argv[3]);

        if (cmd != "considerTable" && cmd != "obsoleteStats")
        {
            cout << "Invalid command" << endl;
        }

        if (cmd == "considerTable")
		{
			map<string, string> result = goutil.considerTable(argv[1]);

			for (auto pair : result)
			{ 
				cout << pair.first << "\t" << pair.second << endl;
			}
		}
        if (cmd == "obsoleteStats")
        {
            map<int, int> counter = goutil.obsoleteStats(argv[1]);

			for (auto pair : counter)
			{ 
				cout << "consider \t" << pair.first << endl;
                cout << "no-consider \t" << pair.second << endl;
			}
        }

        regex pat("^.tab");
        if (regex_search(option, pat))
        {
            map<string, string> result = goutil.considerTable(argv[1]);

            ofstream stream(option);
            for(auto& kv : result) 
            {
                stream << kv.first << "\t" << kv.second << '\n';
            }
            stream.close();
        }

	    return 0;
    }
}