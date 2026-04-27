# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git81
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


#include <bits/stdc++.h>
using namespace std;
int main(){
	int a[10],b[42]={},s=0;
	for(int i=0;i<10;i++) cin>>a[i];
	for(int i=0;i<10;i++){
		b[a[i]%42]++;
	}
	for(int i=0;i<42;i++){
		if(b[i]>0)s++;
	}
	cout<<s;
}
