# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git75
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,k;
	cin>>n>>k;
	n--;
	int h=k/n;
	if(h*n==k){
		cout<<k+h-1<<" "<<h+k;
	}
	else{
		cout<<h+k<<" "<<h+k;
	}
}
